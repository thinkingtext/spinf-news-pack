#!/usr/bin/env python3
"""Build the thinkingtext news packs: the published question sets of tt-news-index (the OIL-F6 and EQ-S10 news indexes) exported as
spinf prompt packs, standardised on a public news sample, with a golden fixture per version.

    python tools/build.py export    --registry ../tt-news-index                      # drafts/<name>.json from the registry and the specs
    python tools/build.py score     --draft drafts/oil.json --inputs calibration/wikinews_business.json.gz --out calibration/answers/oil.jsonl
    python tools/build.py calibrate --draft drafts/oil.json --answers calibration/answers/oil.jsonl --out packs/oil/0.1.0.json
    python tools/build.py samples   --inputs calibration/wikinews_business.json.gz    # packs/<name>/samples/inputs.json, drawn from the sample
    python tools/build.py fixture   --pack packs/oil/0.1.0.json --samples packs/oil/samples/inputs.json --out packs/oil/fixtures/0.1.0.json
    python tools/build.py manifest                                                    # prompt-packs.json from the pack folders
    python tools/build.py readme                                                      # packs/<name>/README.md from the pack files
    python tools/build.py check                                                       # every fixture recomputed with spinf_serve.packs (CI)

The only dependencies are spinf-serve (its `packs` module is pure Python) and, for `export`, PyYAML and a checkout of tt-news-index.
Scoring needs a server: SPINF_URL (default http://localhost:8000, a local spinf-serve serving spinf/gemma-4-12b-fp8) and, for the
hosted API, SPINF_API_KEY.
"""

import argparse
import glob
import gzip
import hashlib
import importlib.util
import json
import math
import os
import random
import re
import sys
import time
import urllib.request

from spinf_serve import packs
from spinf_serve.packs import pipeline

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL = "spinf/gemma-4-12b-fp8"
NAMESPACE = "thinkingtext"
VERSION = "0.1.0"
LEVELS = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99, 0.999, 1]
CONTEXT = {"article": "{X}"}  # the article as it is, nothing before or after it: the index scores the raw text
TOL = 2e-6


# ---------------------------------------------------------------- export: registry + specs -> drafts
def _module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def query_for(template, phrase, pair):
    """registry template '{X}...{F}...' -> (pack template, options): the text after the article, ending in {?}, the pair as the options"""
    assert template.startswith("{X}"), template
    assert "{CTX}" not in template, template
    tail = template[len("{X}") :].format(F=phrase)
    return tail.replace("{", "{{").replace("}", "}}") + "{?}", [" " + pair[0], " " + pair[1]]


def _label(sentence):
    return re.sub(r" (is|are) \{w\}", "", sentence).rstrip(".")


def _draft(pack, name, description, R, cells, reads, categories, origin):
    """the common shape: one query per distinct cell, the reads and categories given, no decision (every category reports only)"""
    queries, meta = [], {}
    for cid in cells:
        c = R["cells"][cid]
        tpl, opts = query_for(R["templates"][c["template"]], c["phrase"], R["pairs"][c["pair"]])
        queries.append({"id": cid, "template": tpl, "options": opts})
        meta[cid] = {"phrase": c["phrase"], "pair": list(R["pairs"][c["pair"]]), "wording": c["template"], "principal": c["principal"]}
    return {
        "pack": f"{NAMESPACE}/{pack}",
        "version": VERSION,
        "model": MODEL,
        "media": ["text"],
        "answers": "logprob",
        "name": name,
        "description": description,
        "origin": origin,
        "contexts": dict(CONTEXT),
        "scoring": {"empty_floor": False, "case_insensitive": False, "queries": queries},
        "cells": meta,
        "reads": reads,
        "categories": categories,
        "decision": {"mode": "per_category", "fallback": "per_category", "critical": []},
    }


def export(a):
    reg_dir = os.path.abspath(a.registry)
    sys.path.insert(0, reg_dir)
    registry = _module(os.path.join(reg_dir, "registry.py"), "tt_registry")
    oil = _module(os.path.join(reg_dir, "publish", "spec.py"), "oil_spec")
    stk = _module(os.path.join(reg_dir, "publish", "stock_spec.py"), "stock_spec")
    R = registry.load_registry(reg_dir)
    today = time.strftime("%Y-%m-%d")
    out = {}

    # oil: the 18 slots of OIL-F6 (the physical six that make f6, and the context slots), each a category of its cells; f6 = the six
    cells, reads, cats = [], [], {}
    for slot, sentence, words, cl in oil.SLOTS:
        cats[slot] = {"label": _label(sentence), "sentence": sentence, "words": list(words), "deciding": False, "role": "index" if slot in oil.SIX else "context"}
        for cid, sign in cl:
            assert cid in R["cells"], cid
            if cid not in cells:
                cells.append(cid)
            reads.append({"id": f"{slot}/{cid}", "query": cid, "kind": "pair", "sign": sign, "category": slot})
            if slot in oil.SIX:
                reads.append({"id": f"f6/{slot}/{cid}", "query": cid, "kind": "pair", "sign": sign * oil.SIX[slot], "category": "f6", "view": slot})
    cats["f6"] = {
        "label": "Oil news read (F6)",
        "aggregate": "views",
        "words": list(oil.F6_WORDS),
        "slots": {s: oil.SIX[s] for s in oil.SIX},
        "deciding": False,
        "role": "composite",
    }
    origin = {
        "index": oil.NAME,
        "long_name": oil.LONG_NAME,
        "spec_version": oil.SPEC_VERSION,
        "registry": "thinkingtext/tt-news-index",
        "registry_md5": registry.registry_md5(R, cells),
        "exported": today,
    }
    out["oil"] = _draft(
        "oil",
        "Oil news",
        "The questions of the OIL-F6 oil news index: 18 slots (demand, supply, inventories, OPEC+, disruption risk, refining margins, and the macro context) read on an article, and the signed six-slot composite.",
        R, cells, reads, cats, origin,
    )

    # equities: one pack per published name of EQ-S10, a category per slot family and the company composite
    F = stk.cells()
    for code in stk.PUBLISHED:
        slots = F["names"][code]["slots"]
        cells, reads, cats = [], [], {}
        for fam in stk.SLOT_FAMILIES:
            if fam not in slots:
                continue
            cats[fam] = {"label": stk.SLOT_SENTENCE[fam], "deciding": False, "role": "slot"}
            for cid, sign in slots[fam].items():
                assert cid in R["cells"], cid
                if cid not in cells:
                    cells.append(cid)
                reads.append({"id": f"{fam}/{cid}", "query": cid, "kind": "pair", "sign": sign, "category": fam})
                reads.append({"id": f"company/{fam}/{cid}", "query": cid, "kind": "pair", "sign": sign, "category": "company", "view": fam})
        cats["company"] = {"label": f"{stk.COMPANY[code]} news read", "aggregate": "views", "words": list(stk.INDEX_WORDS), "deciding": False, "role": "composite"}
        origin = {
            "index": stk.NAME,
            "long_name": stk.LONG_NAME,
            "spec_version": stk.SPEC_VERSION,
            "company": stk.COMPANY[code],
            "ticker": stk.TICKER[code],
            "peers": [stk.TICKER[p] for p in F["names"][code]["peers"]],
            "weights": {"company": round(1 - stk.MARKET_WEIGHT - (stk.PEER_WEIGHT if F["names"][code]["peers"] else 0), 2), "peers": stk.PEER_WEIGHT if F["names"][code]["peers"] else 0, "market": stk.MARKET_WEIGHT},
            "registry": "thinkingtext/tt-news-index",
            "registry_md5": registry.registry_md5(R, cells),
            "exported": today,
        }
        out[f"equity-{code}"] = _draft(
            f"equity-{code}",
            f"{stk.COMPANY[code]} news",
            f"The {stk.COMPANY[code]} ({stk.TICKER[code]}) questions of the EQ-S10 equity news index: the company's steady cells by slot family, read on an article about the company, and their composite.",
            R, cells, reads, cats, origin,
        )

    # the general market read: the cells read against QQQ on the general news flow
    cells, reads = [], []
    for cid, sign in F["market_read"].items():
        assert cid in R["cells"], cid
        cells.append(cid)
        reads.append({"id": f"market/{cid}", "query": cid, "kind": "pair", "sign": sign, "category": "market"})
    cats = {"market": {"label": "General market read", "words": list(stk.INDEX_WORDS), "deciding": False, "role": "composite"}}
    origin = {
        "index": stk.NAME,
        "long_name": stk.LONG_NAME,
        "spec_version": stk.SPEC_VERSION,
        "part": "market_read",
        "registry": "thinkingtext/tt-news-index",
        "registry_md5": registry.registry_md5(R, cells),
        "exported": today,
    }
    out["market"] = _draft(
        "market",
        "Market news",
        f"The general market read of the EQ-S10 equity news index: {len(cells)} macro and market cells, signed toward higher US stock prices, read on business news.",
        R, cells, reads, cats, origin,
    )

    for name, d in out.items():
        problems = packs.validate(d, draft=True)
        assert not problems, (name, problems)
        os.makedirs(os.path.join(ROOT, a.out), exist_ok=True)
        with open(os.path.join(ROOT, a.out, f"{name}.json"), "w") as f:
            json.dump(d, f, indent=1, ensure_ascii=False)
            f.write("\n")
        print(f"{name:14s} {len(d['scoring']['queries']):3d} queries, {len(d['reads']):3d} reads, {len(d['categories']):2d} categories")


# ---------------------------------------------------------------- score: a draft on the sample
def post(url, body, key):
    headers = {"Content-Type": "application/json"}
    if key:
        headers["Authorization"] = f"Bearer {key}"
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=1800) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code}: {e.read().decode(errors='replace')[:2000]}") from None


def load_sample(path, limit=0, seed=0):
    with gzip.open(path, "rt") as f:
        arts = json.load(f)["articles"]
    if limit and len(arts) > limit:
        arts = random.Random(seed).sample(arts, limit)
        arts.sort(key=lambda x: x["id"])
    return arts


def score(a):
    url = os.environ.get("SPINF_URL", "http://localhost:8000").rstrip("/") + "/v1/score"
    key = os.environ.get("SPINF_API_KEY") or None
    pack = packs.load(a.draft, draft=True)
    arts = load_sample(a.inputs, a.limit, a.seed)
    done = set()
    if os.path.exists(a.out):
        with open(a.out) as f:
            done = {json.loads(x)["id"] for x in f if x.strip()}
    todo = [x for x in arts if x["id"] not in done]
    print(f"{pack.id}: {len(arts)} inputs, {len(done)} scored, {len(todo)} to score at {url}", flush=True)
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    t0 = time.time()
    with open(a.out, "a") as out:
        for i in range(0, len(todo), a.batch):
            chunk = todo[i : i + a.batch]
            body = pack.request([x["text"] for x in chunk], "article", ids=[x["id"] for x in chunk], model=a.model)
            resp = post(url, body, key)
            by_id = {r["input_id"]: r for r in resp["results"]}
            for x in chunk:
                ans = pipeline.answers_from_result(by_id[x["id"]], set(pack.query_ids), "logprob")
                row = {"id": x["id"], "engine": resp.get("system_fingerprint"), "ans": {q: [math.log(max(p, 1e-300)) for p in ps] for (q, _), ps in ans.items()}}
                out.write(json.dumps(row) + "\n")
            out.flush()
            print(f"  {min(i + a.batch, len(todo))}/{len(todo)}  {time.time() - t0:.0f}s", flush=True)
    print("DONE")


# ---------------------------------------------------------------- calibrate: draft + answers -> the pack
def load_rows(path):
    rows = []
    with open(path) as f:
        for line in f:
            if line.strip():
                r = json.loads(line)
                r["ans"] = {(q, None): [math.exp(v) for v in lp] for q, lp in r["ans"].items()}
                rows.append(r)
    return rows


def quantile(xs, q):
    """numpy's default (linear) quantile of a sorted list"""
    pos = q * (len(xs) - 1)
    lo = math.floor(pos)
    hi = min(lo + 1, len(xs) - 1)
    return xs[lo] + (xs[hi] - xs[lo]) * (pos - lo)


def calibrate(a):
    with open(a.draft) as f:
        pack = json.load(f)
    rows = load_rows(a.answers)
    engines = {}
    for r in rows:
        engines[r["engine"]] = engines.get(r["engine"], 0) + 1
    if len(engines) > 1:
        print(f"WARNING: answers from more than one engine: {engines}")
    pack["engine"] = max(engines, key=engines.get)
    for r in pack["reads"]:
        v = [pipeline.read_value(r, x["ans"]) for x in rows]
        m = sum(v) / len(v)
        sd = math.sqrt(sum((x - m) ** 2 for x in v) / len(v))
        r["mean"], r["sd"] = round(m, 5), round(sd + 1e-9, 5)
    for c, spec in pack["categories"].items():
        spec.pop("deciding", None)
        spec["platt"] = [1.0, 0.0]  # score = sigmoid(mean z): logit(score) gives the category's z back
        spec["fit_platt"] = False
        spec["uncalibrated"] = True
        spec["threshold"] = None
    macros = [pipeline.category_macros(pack, pipeline.read_z(pack, x["ans"])) for x in rows]
    for c, spec in pack["categories"].items():
        s = sorted(1 / (1 + math.exp(-m[c])) for m in macros)
        spec["normal_quantiles"] = {"levels": LEVELS, "values": [round(quantile(s, q), 5) for q in LEVELS]}
    pack["decision"] = {"mode": "per_category", "fallback": "per_category", "critical": [], "per_category": {}}
    pack["calibration"] = {"sample": os.path.relpath(a.sample, ROOT) if a.sample else "calibration/wikinews_business.json.gz", "n": len(rows), "statistic": "mean and sd of each read over the sample; no thresholds, no decision", "date": time.strftime("%Y-%m-%d")}
    problems = packs.validate(pack)
    assert not problems, problems
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    with open(a.out, "w") as f:
        json.dump(pack, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print(f"{pack['pack']} {pack['version']}: {len(pack['scoring']['queries'])} queries, {len(pack['reads'])} reads, {len(pack['categories'])} categories, {len(rows)} normal rows, engine {pack['engine']}")
    for c, spec in pack["categories"].items():
        v = spec["normal_quantiles"]["values"]
        print(f"  {c:14s} median {v[LEVELS.index(0.5)]:.3f}  p10 {v[LEVELS.index(0.1)]:.3f}  p90 {v[LEVELS.index(0.9)]:.3f}")


# ---------------------------------------------------------------- samples: the shipped inputs, drawn from the sample
ALIASES = {"meta": ("Facebook",), "googl": ("Google",), "amd": ("Advanced Micro Devices",)}  # the names Wikinews uses
SAMPLE_PICK = {
    # pack folder: (tags that admit an article, words that must appear, how many)
    "oil": (("cat:OPEC", "search:oil", "cat:Energy"), ("oil", "crude", "OPEC", "barrel"), 6),
    "market": (("search:stocks", "cat:Economy_and_business"), ("stock", "Wall Street", "Nasdaq", "Dow Jones", "shares"), 6),
}


def samples(a):
    arts = load_sample(a.inputs)
    for draft_path in sorted(glob.glob(os.path.join(ROOT, "drafts", "*.json"))):
        name = os.path.basename(draft_path)[:-5]
        folder = os.path.join(ROOT, "packs", name)
        with open(draft_path) as f:
            d = json.load(f)
        if name in SAMPLE_PICK:
            tags, words, n = SAMPLE_PICK[name]
        else:
            code = name.split("-", 1)[1]
            company = d["origin"]["company"]
            tags, words, n = (f"search:{code}",), (company, *ALIASES.get(code, ())), 5
        cands = []
        for x in arts:
            if not any(t in x["tags"] for t in tags):
                continue
            hits = sum(x["text"].count(w) for w in words)
            if hits:
                cands.append((hits, len(x["text"].split()) <= 450, x))
        cands.sort(key=lambda t: (-t[0], -t[1], t[2]["id"]))
        picked = [x for _, _, x in cands[:n]]
        out = [{"id": x["id"], "context": "article", "text": x["text"], "source": {"title": x["title"], "url": x["url"], "revision": x["revision"], "license": "CC BY 2.5"}} for x in picked]
        if len(out) < 3 and name.startswith("equity-"):  # Wikinews rarely covers some names: illustrative articles written by thinkingtext
            with open(os.path.join(ROOT, "calibration", "synthetic_samples.json")) as f:
                syn = json.load(f).get(name.split("-", 1)[1], [])
            out += [{"id": x["id"], "context": "article", "text": x["text"], "source": {"title": x["title"], "license": "written by thinkingtext, illustrative (not a news report)"}} for x in syn]
        os.makedirs(os.path.join(folder, "samples"), exist_ok=True)
        with open(os.path.join(folder, "samples", "inputs.json"), "w") as f:
            json.dump(out, f, indent=1, ensure_ascii=False)
            f.write("\n")
        print(f"{name:14s} {len(out)} samples ({len(picked)} Wikinews from {len(cands)} candidates): " + "; ".join(x["source"]["title"][:40] for x in out))


# ---------------------------------------------------------------- fixture: the samples scored, the evaluator's output per mode
def fixture(a):
    url = os.environ.get("SPINF_URL", "http://localhost:8000").rstrip("/") + "/v1/score"
    key = os.environ.get("SPINF_API_KEY") or None
    pack = packs.load(a.pack)
    with open(a.samples) as f:
        items = json.load(f)
    body = pack.request([s["text"] for s in items], "article", ids=[s["id"] for s in items], model=a.model)
    resp = post(url, body, key)
    by_id = {r["input_id"]: r for r in resp["results"]}
    cases = []
    for s in items:
        res = by_id[s["id"]]
        ans = pack.answers(res)
        expected = {m: {k: v for k, v in pack.evaluate(ans, m).items() if k in ("categories", "decision")} for m in pack.modes}
        cases.append({"id": s["id"], "text": s["text"], "context": "article", "source": s.get("source"), "result": res, "expected": expected})
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with open(a.out, "w") as f:
        json.dump({"pack": pack.id, "version": pack.version, "engine": resp.get("system_fingerprint"), "usage": resp.get("usage"), "cases": cases}, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print(f"wrote {a.out}: {len(cases)} cases, engine {resp.get('system_fingerprint')}, {os.path.getsize(a.out) / 1024:.0f} KB")


# ---------------------------------------------------------------- manifest and check
def pack_folders():
    out = []
    for folder in sorted(glob.glob(os.path.join(ROOT, "packs", "*"))):
        versions = sorted(glob.glob(os.path.join(folder, "*.json")), key=lambda p: [int(x) if x.isdigit() else x for x in re.split(r"[.]", os.path.basename(p)[:-5])], reverse=True)
        if versions:
            out.append((folder, versions))
    return out


def manifest(a):
    entries = []
    order = {"oil": 0, "market": 1}
    for folder, versions in sorted(pack_folders(), key=lambda t: (order.get(os.path.basename(t[0]), 2), t[0])):
        name = os.path.basename(folder)
        with open(versions[0]) as f:
            d = json.load(f)
        vs = []
        for p in versions:
            with open(p) as f:
                v = json.load(f)
            fx = os.path.join(folder, "fixtures", f"{v['version']}.json")
            e = {"version": v["version"], "file": os.path.relpath(p, ROOT), "model": v["model"], "status": "available"}
            if os.path.exists(fx):
                e["fixture"] = os.path.relpath(fx, ROOT)
            vs.append(e)
        tags = ["news", "finance"] + (["oil", "commodities"] if name == "oil" else ["equities"])
        entry = {"id": d["pack"], "name": d["name"], "description": d["description"], "tags": tags, "media": ["text"], "readme": f"packs/{name}/README.md"}
        if os.path.exists(os.path.join(folder, "samples", "inputs.json")):
            entry["samples"] = f"packs/{name}/samples/"
        entry["versions"] = vs
        entries.append(entry)
    m = {"format": 1, "namespace": NAMESPACE, "name": "thinkingtext news packs", "homepage": "https://github.com/thinkingtext/spinf-news-pack", "license": "Apache-2.0", "packs": entries}
    with open(os.path.join(ROOT, "prompt-packs.json"), "w") as f:
        json.dump(m, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print(f"prompt-packs.json: {len(entries)} packs")


def check(a):
    """every fixture recomputed from its raw results with the evaluator; a mismatch is a failure (exit 1)"""
    bad = 0
    with open(os.path.join(ROOT, "prompt-packs.json")) as f:
        m = json.load(f)
    for e in m["packs"]:
        for v in e["versions"]:
            if "fixture" not in v:
                print(f"{e['id']} {v['version']}: no fixture")
                bad += 1
                continue
            pack = packs.load(os.path.join(ROOT, v["file"]))
            with open(os.path.join(ROOT, v["fixture"])) as f:
                fx = json.load(f)
            n = 0
            for case in fx["cases"]:
                ans = pack.answers(case["result"])
                for mode, exp in case["expected"].items():
                    got = pack.evaluate(ans, mode)
                    for c, ev in exp["categories"].items():
                        gv = got["categories"][c]
                        if abs(gv["score"] - ev["score"]) > TOL or abs((gv["percentile"] or 0) - (ev["percentile"] or 0)) > TOL or gv["flagged"] != ev["flagged"]:
                            print(f"  {e['id']} {case['id']} {mode} {c}: {gv} != {ev}")
                            n += 1
                    if got["decision"] != exp["decision"]:
                        print(f"  {e['id']} {case['id']} {mode} decision: {got['decision']} != {exp['decision']}")
                        n += 1
            print(f"{e['id']} {v['version']}: {len(fx['cases'])} cases, {n} mismatches, engine {fx['engine']}")
            bad += n
    sys.exit(1 if bad else 0)


# ---------------------------------------------------------------- readme
def _cells_table(d, reads_of):
    rows = []
    for r in reads_of:
        c = d["cells"][r["query"]]
        arrow = f"{c['pair'][0]} / {c['pair'][1]}"
        rows.append(f"| `{r['query']}` | {c['phrase']} | {arrow} | {'+' if r['sign'] > 0 else '−'} | {c['wording']} |")
    return rows


def readme(a):
    for folder, versions in pack_folders():
        name = os.path.basename(folder)
        with open(versions[0]) as f:
            d = json.load(f)
        o = d["origin"]
        cal = d.get("calibration", {})
        n_q = len(d["scoring"]["queries"])
        lines = [f"# {d['pack']}: {d['name']}", ""]
        if name == "oil":
            lines += [
                f"The question set of **{o['long_name']} ({o['index']})**, the daily oil news index of thinkingtext, as a prompt pack. The index reads",
                f"every oil-market article of the day with these {n_q} questions and publishes the signed six-slot composite with its context slots;",
                "this pack gives the same reads on any article you send, in one call, next to your own questions.",
                "",
                "Each question is a *cell*: the article, then a short sentence that ends where a one-word answer goes, with two single-token",
                'answers of opposite direction (`" increase"` / `" decrease"`, `" rise"` / `" fall"`, `" tighten"` / `" ease"`). The read is the',
                "log-odds of the first answer over the second, signed toward the slot's \"up\" word. A slot is the mean of its cells' standardised",
                "reads; `f6` is the mean of the six physical slots, each signed toward a **higher oil price** (demand +, supply −, inventories −,",
                "OPEC+ quotas +, disruption risk +, refining margins +).",
            ]
        elif name == "market":
            lines += [
                f"The **general market read** of {o['long_name']} ({o['index']}), the equity news index of thinkingtext, as a prompt pack: {n_q} macro",
                "and market cells (growth, rates, inflation, earnings, risk appetite, currencies, commodities, trade), each signed toward higher US",
                "stock prices, read on business news. In the index this read is one third of every company's index and is published on its own",
                "against the Nasdaq-100.",
            ]
        else:
            lines += [
                f"The **{o['company']} ({o['ticker']})** questions of {o['long_name']} ({o['index']}), the equity news index of thinkingtext, as a",
                f"prompt pack: the company's {n_q} *steady* cells, those whose daily read moved with the share price in every year of the research",
                "window, by slot family, read on an article about the company. The reads are whole-article wordings (\"Summary of the key facts in",
                "the article above, from beginning to end, and their consequence: ... is likely to\") with two single-token answers of opposite",
                "direction; each is signed toward a **higher share price**.",
            ]
        lines += [
            "",
            f"Model: `{d['model']}`. Media: text. Context: `article` (the text as it is: the index sends the article's first 260 words; the pack",
            "takes any length the server allows). No decision: every category is reported with a score and a percentile and none flags.",
            "",
            "## Reading the scores",
            "",
            "A category's `score` is `sigmoid(z)`, where `z` is the mean over its cells of each read standardised on the calibration sample",
            f"(`logit(score)` gives `z` back; `score` 0.5 is the sample's typical article). `percentile` places the score among the sample's",
            "articles. The reads themselves come back with `include_queries: true`: each cell's two answers with their log-probabilities, so",
            "`logprob(first) − logprob(second)` is the raw read the index works from.",
            "",
            "What the index does with them, and this pack does not: the daily mean of each cell over the day's gated articles, a trailing",
            "robust z over 250 days, an exponential smoothing, the composite's state words and the price regressions. Those live in the index's",
            "code ([thinkingtext/tt-news-index](https://github.com/thinkingtext/tt-news-index)); the pack is the question set and the per-read baselines.",
            "",
            "## Categories",
            "",
        ]
        if name == "oil":
            lines += ["| id | slot | role | cells | state words |", "|---|---|---|---|---|"]
            for c, spec in d["categories"].items():
                cells = sorted({r["query"] for r in d["reads"] if r["category"] == c})
                lines.append(f"| `{c}` | {spec['label']} | {spec.get('role', '')} | {len(cells)} | {', '.join(spec.get('words', []))} |")
        else:
            lines += ["| id | family | role | cells |", "|---|---|---|---|"]
            for c, spec in d["categories"].items():
                cells = sorted({r["query"] for r in d["reads"] if r["category"] == c})
                lines.append(f"| `{c}` | {spec['label']} | {spec.get('role', '')} | {len(cells)} |")
        lines += ["", "## Cells", "", "| cell | phrase | answers | sign | wording |", "|---|---|---|---|---|"]
        seen = set()
        base = [r for r in d["reads"] if not r.get("view")] or d["reads"]
        for r in base:
            if r["query"] in seen:
                continue
            seen.add(r["query"])
            lines += _cells_table(d, [r])
        lines += [
            "",
            "Wordings: `default` = *\"{article}\\n\\nAs a result, {phrase} is likely to\"*; `summary` = *\"{article}\\n\\nSummary of the key facts in the",
            "article above, from beginning to end, and their consequence: {phrase} is likely to\"*; `sum_news_co` = *\"... for {company} shareholders,",
            "this news is\"* (positive / negative); `sum_expect` = *\"... relative to market expectations, {phrase} came in\"* (higher / lower).",
            "The sign is the direction of the first answer toward the category's \"up\" (a higher oil price, a higher share price).",
        ]
        if name.startswith("equity-"):
            w = o["weights"]
            lines += [
                "",
                "## The index formula",
                "",
                f"EQ-S10 for {o['company']} = {w['company']} × the company read (`company`: the mean of the non-empty slot families on the day's articles"
                + (f") + {w['peers']} × the peers' company reads ({', '.join(o['peers'])})" if o["peers"] else ")")
                + f" + {w['market']} × the general market read (`thinkingtext/market`), each a trailing robust z; the state words are "
                + ", ".join(d["categories"]["company"]["words"]) + ".",
            ]
        lines += [
            "",
            "## Calibration",
            "",
            f"Standardised on {cal.get('n', '?')} Wikinews business, economy, energy and company articles (CC BY 2.5; `{cal.get('sample', '')}`),",
            f"scored on {d.get('engine', '?')} on {cal.get('date', '')}. Nothing is fitted on labels or prices: the index's own article data stays",
            f"with the index. Exported from the tt-news-index registry (spec {o['spec_version']}, registry md5 `{o['registry_md5'][:8]}`) on {o['exported']}.",
            "",
            "## Files",
            "",
            f"`{os.path.relpath(versions[0], folder)}` the pack; `samples/inputs.json` the articles the fixture scores: Wikinews articles (CC BY 2.5, attributed in each",
            "entry) and, for companies Wikinews rarely covers, illustrative articles written by thinkingtext (marked as such; not news reports);",
            f"`fixtures/{d['version']}.json` the samples' raw results and the evaluator's output.",
            "",
        ]
        with open(os.path.join(folder, "README.md"), "w") as f:
            f.write("\n".join(lines))
        print(f"{name}: README written")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("export")
    p.add_argument("--registry", required=True, help="a checkout of thinkingtext/tt-news-index")
    p.add_argument("--out", default="drafts")
    p.set_defaults(fn=export)
    p = sub.add_parser("score")
    p.add_argument("--draft", required=True)
    p.add_argument("--inputs", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--limit", type=int, default=0, help="a random subset of the sample (seeded)")
    p.add_argument("--seed", type=int, default=20261024)
    p.add_argument("--batch", type=int, default=32)
    p.add_argument("--model", default=None, help="the server's name of the model when it differs (the hosted API)")
    p.set_defaults(fn=score)
    p = sub.add_parser("calibrate")
    p.add_argument("--draft", required=True)
    p.add_argument("--answers", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--sample", default=None, help="the sample file the answers came from (recorded in the pack)")
    p.set_defaults(fn=calibrate)
    p = sub.add_parser("samples")
    p.add_argument("--inputs", required=True)
    p.set_defaults(fn=samples)
    p = sub.add_parser("fixture")
    p.add_argument("--pack", required=True)
    p.add_argument("--samples", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--model", default=None)
    p.set_defaults(fn=fixture)
    sub.add_parser("manifest").set_defaults(fn=manifest)
    sub.add_parser("readme").set_defaults(fn=readme)
    sub.add_parser("check").set_defaults(fn=check)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
