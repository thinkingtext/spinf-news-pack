# thinkingtext news packs

The question sets behind thinkingtext's news indexes, published as [spinf prompt packs](https://github.com/spinfinc/spinf-prompts/blob/main/docs/prompt-packs.md)
for [spinf-serve](https://github.com/spinfinc/spinf-serve) and the hosted spinf API. A pack is named in a scoring request and
answered in the same read of the article as your own questions; it returns one standardised score and percentile per slot, and the
raw reads with `include_queries: true`.

**Where to look.** The questions of a pack, written out, are in `packs/<name>/QUESTIONS.md`; the file a server loads is
`packs/<name>/<version>.json`, described in `packs/<name>/README.md`. Everything else in a pack folder is test material (sample
articles and their expected results), and everything under `sources/` is how the packs are made.

| pack | what it reads | from | model |
|---|---|---|---|
| [`thinkingtext/oil`](packs/oil/) | an oil-market article: demand, supply, inventories, OPEC+, disruption risk, refining margins, the macro context; the signed six-slot composite `f6` | OIL-F6, the oil news index (spec 1.1) | `spinf/gemma-4-12b-fp8` |
| [`thinkingtext/equity-<ticker>`](packs/) | an article about one company: its steady cells by slot family (demand, profits, outlook, competition, regulation, costs, the share price and valuation, results against expectations, the market and macro read) and their composite. Twelve names: `tsla`, `nvda`, `amd`, `meta`, `intc`, `googl`, `aapl`, `mu`, `msft`, `pltr`, `amzn`, `csco` | EQ-S10, the equity news index (spec 1.2) | `spinf/gemma-4-12b-fp8` |
| [`thinkingtext/market`](packs/market/) | business news: the general market read, 126 macro and market cells signed toward higher US stock prices | EQ-S10, the general market read | `spinf/gemma-4-12b-fp8` |

Every question is a *cell*: the article, then a short sentence ending where a one-word answer goes, with two single-token answers
of opposite direction. The engine returns both answers' log-probabilities; the pack standardises their difference on a sample of
public news and averages the cells of a slot. No pack decides anything: the categories report, the thresholds are null.

## Use

```sh
spinf-serve serve spinf/gemma-4-12b-fp8 --packs github:thinkingtext/spinf-news-pack@<tag>
```

```json
{ "model": "spinf/gemma-4-12b-fp8",
  "messages": [ { "role": "user", "content": "<the article>" } ],
  "scoring": { "packs": [ { "id": "thinkingtext/oil", "include_queries": true } ] } }
```

The `oil` and `market` packs and one `equity-*` pack can go in the same call (they share the bare `article` context); send a
company's articles with its pack, and the general flow with `market`. The same call runs against the hosted API with a key.

## What the index does that the pack does not

The indexes select the articles (outlet lists, keyword gates per market, deduplication, the first 260 words), average each cell
over the day's articles, standardise the daily means on a trailing 250-day window, smooth them, and read the result against prices.
All of that is the consumer's side ([thinkingtext/tt-news-index](https://github.com/thinkingtext/tt-news-index)); the packs are the
question sets and per-read baselines, exported from the index's cell registry by `sources/build.py` and re-exported as a new version
whenever the index's specification changes.

## Layout

- `packs/<name>/`: one folder per pack. `<version>.json` is the pack itself, `QUESTIONS.md` its questions written out by category,
  `README.md` what it reads and how to read the scores, `samples/inputs.json` a few Wikinews articles (CC BY 2.5, attributed) and
  `fixtures/<version>.json` their raw results and the evaluator's output, which CI recomputes.
- `prompt-packs.json`: the manifest a server reads (namespace `thinkingtext`).
- `sources/`: the material the packs are built from and the scripts that build them; see `sources/README.md`. A user of the packs
  never needs it.

## Versioning and licence

A pack version never changes once published; a change to a question set or to the calibration is a new version, and a new
index specification a new minor. Apache 2.0 (`LICENSE`); the data the packs were standardised on is credited in
`ACKNOWLEDGEMENTS.md`.
