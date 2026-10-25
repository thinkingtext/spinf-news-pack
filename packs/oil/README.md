# thinkingtext/oil: Oil news

The question set of **Oil News Index F6 (OIL-F6)**, the daily oil news index of thinkingtext, as a prompt pack. The index reads
every oil-market article of the day with these 43 questions and publishes the signed six-slot composite with its context slots;
this pack gives the same reads on any article you send, in one call, next to your own questions.

Each question is a *cell*: the article, then a short sentence that ends where a one-word answer goes, with two single-token
answers of opposite direction (`" increase"` / `" decrease"`, `" rise"` / `" fall"`, `" tighten"` / `" ease"`). The read is the
log-odds of the first answer over the second, signed toward the slot's "up" word. A slot is the mean of its cells' standardised
reads; `f6` is the mean of the six physical slots, each signed toward a **higher oil price** (demand +, supply −, inventories −,
OPEC+ quotas +, disruption risk +, refining margins +).

Model: `spinf/gemma-4-12b-fp8`. Media: text. Context: `article` (the text as it is: the index sends the article's first 260 words; the pack
takes any length the server allows). No decision: every category is reported with a score and a percentile and none flags.

## Reading the scores

A category's `score` is `sigmoid(z)`, where `z` is the mean over its cells of each read standardised on the calibration sample
(`logit(score)` gives `z` back; `score` 0.5 is the sample's typical article). `percentile` places the score among the sample's
articles. The reads themselves come back with `include_queries: true`: each cell's two answers with their log-probabilities, so
`logprob(first) − logprob(second)` is the raw read the index works from.

What the index does with them, and this pack does not: the daily mean of each cell over the day's gated articles, a trailing
robust z over 250 days, an exponential smoothing, the composite's state words and the price regressions. Those live in the index's
code ([thinkingtext/tt-news-index](https://github.com/thinkingtext/tt-news-index)); the pack is the question set and the per-read baselines.

## Categories

| id | slot | role | cells | state words |
|---|---|---|---|---|
| `demand` | Global oil demand | index | 3 | falling sharply, falling, steady, rising, rising sharply |
| `supply` | Global oil supply | index | 4 | falling sharply, falling, steady, rising, rising sharply |
| `inventories` | US oil inventories | index | 4 | falling sharply, falling, steady, rising, rising sharply |
| `opec` | OPEC+ production quotas | index | 1 | easing sharply, easing, unchanged, tightening, tightening sharply |
| `disruption` | The risk of oil supply disruptions | index | 4 | falling sharply, falling, steady, rising, rising sharply |
| `growth` | The global economy | context | 4 | slowing sharply, slowing, steady, accelerating, accelerating sharply |
| `rates` | US interest rates | context | 2 | falling sharply, falling, steady, rising, rising sharply |
| `dollar` | The US dollar | context | 2 | weakening sharply, weakening, steady, strengthening, strengthening sharply |
| `stocks` | Stock markets | context | 2 | falling sharply, falling, steady, rising, rising sharply |
| `mood` | Investor sentiment | context | 5 | very pessimistic, pessimistic, neutral, optimistic, very optimistic |
| `margins` | Refining margins | index | 2 | falling sharply, falling, steady, rising, rising sharply |
| `inflation` | US inflation | context | 1 | falling sharply, falling, steady, rising, rising sharply |
| `fedcuts` | Expectations of Federal Reserve rate cuts | context | 2 | falling sharply, falling, steady, rising, rising sharply |
| `gold` | Gold prices | context | 1 | falling sharply, falling, steady, rising, rising sharply |
| `euro` | The euro against the dollar | context | 2 | weakening sharply, weakening, steady, strengthening, strengthening sharply |
| `geopolitics` | Geopolitical tensions | context | 2 | easing sharply, easing, unchanged, escalating, escalating sharply |
| `trade` | Trade tensions | context | 2 | easing sharply, easing, unchanged, escalating, escalating sharply |
| `volatility` | Financial market volatility | context | 2 | falling sharply, falling, steady, rising, rising sharply |
| `f6` | Oil news read (F6) | composite | 18 | very bearish, bearish, balanced, bullish, very bullish |

## Questions

The 43 questions, written out as the model sees them and grouped by category, are in [`QUESTIONS.md`](QUESTIONS.md).

## Calibration

Standardised on 1500 Wikinews business, economy, energy and company articles (CC BY 2.5; `sources/calibration/wikinews_business.json.gz`),
scored on fp_51319d2ff6 on 2026-10-24. Nothing is fitted on labels or prices: the index's own article data stays
with the index. Exported from the tt-news-index registry (spec 1.1, registry md5 `a1607d16`) on 2026-10-24.

## Files

`0.1.0.json` the pack, the file a server loads; `QUESTIONS.md` its questions written out; `samples/inputs.json` the articles the fixture scores: Wikinews articles (CC BY 2.5, attributed in each
entry) and, for companies Wikinews rarely covers, illustrative articles written by thinkingtext (marked as such; not news reports);
`fixtures/0.1.0.json` the samples' raw results and the evaluator's output.
