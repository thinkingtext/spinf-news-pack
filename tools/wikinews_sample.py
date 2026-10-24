#!/usr/bin/env python3
"""Fetch the calibration sample: Wikinews business, economy, energy and company articles (CC BY 2.5), cleaned to plain prose.

    python tools/wikinews_sample.py --out calibration/wikinews_business.json.gz

Wikinews text is published under the Creative Commons Attribution 2.5 licence; every article is recorded with its title, URL and
revision. The sample is the "normal traffic" the packs' reads are standardised on (each read's mean and sd), and the shipped
samples of each pack are drawn from it. Articles come from the categories below and from a full-text search for each covered
company; an article is kept when it is plain prose of 100 to 700 words after the dateline, the "Sources" / "Related news" sections
and the Wikinews boilerplate are removed. `tags` says which categories and searches brought the article in.
"""

import argparse
import gzip
import json
import re
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

API = "https://en.wikinews.org/w/api.php"
UA = "spinf-news-pack calibration sample (https://github.com/thinkingtext/spinf-news-pack)"
CATEGORIES = ["Economy_and_business", "Energy", "OPEC", "Apple_Inc.", "Microsoft", "Google", "Facebook", "Amazon.com", "Intel", "Tesla_Motors"]
SEARCHES = {
    "nvda": "Nvidia", "amd": '"Advanced Micro Devices" OR AMD chips', "mu": '"Micron Technology"', "tsla": "Tesla electric", "pltr": "Palantir",
    "csco": '"Cisco Systems"', "meta": '"Meta Platforms" OR Facebook', "googl": "Google OR Alphabet", "amzn": "Amazon.com", "aapl": "Apple iPhone",
    "intc": "Intel chips", "msft": "Microsoft", "oil": "oil prices OPEC crude", "stocks": "stock market Wall Street Nasdaq",
}
CUT_SECTIONS = ("== Sources ==", "== Source ==", "== Related news ==", "== Sister links ==", "== External links ==", "== See also ==")
BOILERPLATE = re.compile(
    r"^(Have an opinion on this story\?.*|Share it!.*|This article (features|is based on|mentions).*|Wikinews .*|"
    r"(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday), [A-Z][a-z]+ \d{1,2}, \d{4}\s*)$"
)


def api(**params) -> dict:
    params = {"format": "json", "formatversion": "2", **params}
    req = urllib.request.Request(API + "?" + urllib.parse.urlencode(params), headers={"User-Agent": UA})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001
            if attempt == 4:
                raise
            print(f"  retry ({e})")
            time.sleep(5 * (attempt + 1))


def clean(extract: str) -> str:
    text = extract
    for marker in CUT_SECTIONS:
        i = text.find(marker)
        if i >= 0:
            text = text[:i]
    lines = []
    for line in text.split("\n"):
        line = line.strip()
        if not line or BOILERPLATE.match(line) or line.startswith("=="):
            continue
        lines.append(line)
    return "\n".join(lines).strip()


def plain_prose(text: str) -> bool:
    words = text.split()
    if not 100 <= len(words) <= 700:
        return False
    if "{{" in text or "[[" in text or "File:" in text:
        return False
    letters = sum(c.isalpha() for c in text)
    return letters / max(1, len(text)) > 0.72


def members(cat: str) -> list[int]:
    ids, cont = [], {}
    while True:
        r = api(action="query", list="categorymembers", cmtitle=f"Category:{cat}", cmnamespace=0, cmlimit=500, **cont)
        ids += [m["pageid"] for m in r["query"]["categorymembers"]]
        if "continue" not in r:
            return ids
        cont = r["continue"]
        time.sleep(0.3)


def search(q: str, limit: int = 300) -> list[int]:
    ids, off = [], 0
    while off < limit:
        r = api(action="query", list="search", srsearch=q, srnamespace=0, srlimit=50, sroffset=off)
        hits = r["query"]["search"]
        ids += [h["pageid"] for h in hits]
        if len(hits) < 50:
            break
        off += 50
        time.sleep(0.3)
    return ids


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    tags: dict[int, list[str]] = {}
    for cat in CATEGORIES:
        ids = members(cat)
        print(f"category {cat}: {len(ids)} pages", flush=True)
        for i in ids:
            tags.setdefault(i, []).append("cat:" + cat)
    for key, q in SEARCHES.items():
        ids = search(q)
        print(f"search {key} ({q}): {len(ids)} pages", flush=True)
        for i in ids:
            tags.setdefault(i, []).append("search:" + key)
    ids = sorted(tags)
    print(f"{len(ids)} distinct pages to fetch", flush=True)

    def fetch(pid):  # one page per request: the API returns a full extract for one page only (several pages need exintro)
        time.sleep(0.2)
        pages = api(action="query", prop="extracts|revisions|info", explaintext=1, exsectionformat="wiki", rvprop="ids", inprop="url", pageids=pid)["query"]["pages"]
        p = pages[0]
        text = clean(p.get("extract", ""))
        if not plain_prose(text) or "/" in p["title"]:
            return None
        return {"id": f"wn{p['pageid']}", "title": p["title"], "url": p["fullurl"], "revision": p["revisions"][0]["revid"], "tags": tags[p["pageid"]], "text": text}

    out, n = [], 0
    with ThreadPoolExecutor(max_workers=4) as ex:
        for r in ex.map(fetch, ids):
            n += 1
            if r:
                out.append(r)
            if n % 200 == 0:
                print(f"  {n}/{len(ids)} fetched, {len(out)} kept", flush=True)
    out.sort(key=lambda x: x["id"])
    with gzip.open(a.out, "wt") as f:
        json.dump({"license": "Text: Wikinews contributors, CC BY 2.5 (https://creativecommons.org/licenses/by/2.5/)",
                   "fetched": time.strftime("%Y-%m-%d"), "articles": out}, f, ensure_ascii=False)
    words = sum(len(x["text"].split()) for x in out)
    print(f"wrote {a.out}: {len(out)} articles, {words} words; DONE")


if __name__ == "__main__":
    main()
