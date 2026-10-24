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

## Cells

| cell | phrase | answers | sign | wording |
|---|---|---|---|---|
| `world:global_oil_demand` | global oil demand | increase / decrease | + | default |
| `usa:us_oil_demand` | US oil demand | increase / decrease | + | default |
| `china:chinese_oil_demand` | Chinese oil demand | increase / decrease | + | default |
| `world:global_oil_supply` | global oil supply | increase / decrease | + | default |
| `opec:opec_crude_oil_production` | OPEC+ crude oil production | increase / decrease | + | default |
| `shale:us_shale_oil_production` | US shale oil production | increase / decrease | + | default |
| `nonopec:non_opec_oil_supply` | non-OPEC oil supply | increase / decrease | + | default |
| `us:us_crude_oil_inventories` | US crude oil inventories | rise / fall | + | default |
| `cushing:crude_oil_inventories_at_cushing_oklahom` | crude oil inventories at Cushing, Oklahoma | rise / fall | + | default |
| `gasoline:us_gasoline_inventories` | US gasoline inventories | rise / fall | + | default |
| `diesel:us_distillate_inventories` | US distillate inventories | rise / fall | + | default |
| `opec:opec_production_quotas` | OPEC+ production quotas | tighten / ease | + | default |
| `mideast:the_risk_of_oil_supply_disruptions_in_th` | the risk of oil supply disruptions in the Middle East | rise / fall | + | default |
| `hormuz:the_risk_of_a_closure_of_the_strait_of_h` | the risk of a closure of the Strait of Hormuz | rise / fall | + | default |
| `russia:the_risk_of_disruption_to_russian_oil_ex` | the risk of disruption to Russian oil exports | rise / fall | + | default |
| `ukraine:the_risk_of_escalation_in_the_war_in_ukr` | the risk of escalation in the war in Ukraine | rise / fall | + | default |
| `world:global_economic_growth` | global economic growth | rise / fall | + | default |
| `usa:us_economic_growth` | US economic growth | rise / fall | + | default |
| `china:china_s_economic_growth` | China's economic growth | rise / fall | + | default |
| `world:the_risk_of_a_global_recession` | the risk of a global recession | rise / fall | − | default |
| `fed:us_interest_rates` | US interest rates | rise / fall | + | default |
| `fed:the_federal_funds_rate` | the federal funds rate | rise / fall | + | default |
| `dollar:the_us_dollar` | the US dollar | rise / fall | + | default |
| `dollar:the_dollar` | the dollar | strengthen / weaken | + | default |
| `stocks:us_stock_prices` | US stock prices | rise / fall | + | default |
| `market:mood_financial_markets` | financial markets | optimism / pessimism | + | mood |
| `market:fear_in_financial_markets` | fear in financial markets | rise / fall | − | default |
| `market:investor_optimism` | investor optimism | rise / fall | + | default |
| `market:risk_aversion_among_investors` | risk aversion among investors | rise / fall | − | default |
| `market:turmoil_in_financial_markets` | turmoil in financial markets | rise / fall | − | default |
| `refiners:global_refining_margins` | global refining margins | rise / fall | + | default |
| `diesel:diesel_prices` | diesel prices | rise / fall | + | default |
| `fed:us_inflation` | US inflation | rise / fall | + | default |
| `fed:expectations_of_fed_rate_cuts` | expectations of Fed rate cuts | rise / fall | + | default |
| `fed:bets_on_federal_reserve_rate_cuts` | bets on Federal Reserve rate cuts | increase / decrease | + | default |
| `gold:gold_prices` | gold prices | rise / fall | + | default |
| `euro:the_euro_against_the_us_dollar` | the euro against the US dollar | rise / fall | + | default |
| `euro:the_euro` | the euro | strengthen / weaken | + | default |
| `market:geopolitical_tensions` | geopolitical tensions | ease / escalate | − | default |
| `market:the_risk_of_a_wider_war` | the risk of a wider war | rise / fall | + | default |
| `market:trade_tensions` | trade tensions | ease / escalate | − | default |
| `trade:us_china_trade_tensions` | US-China trade tensions | rise / fall | − | default |
| `haven:financial_market_volatility` | financial market volatility | rise / fall | + | default |

Wordings: `default` = *"{article}\n\nAs a result, {phrase} is likely to"*; `summary` = *"{article}\n\nSummary of the key facts in the
article above, from beginning to end, and their consequence: {phrase} is likely to"*; `sum_news_co` = *"... for {company} shareholders,
this news is"* (positive / negative); `sum_expect` = *"... relative to market expectations, {phrase} came in"* (higher / lower).
The sign is the direction of the first answer toward the category's "up" (a higher oil price, a higher share price).

## Calibration

Standardised on 1500 Wikinews business, economy, energy and company articles (CC BY 2.5; `calibration/wikinews_business.json.gz`),
scored on fp_51319d2ff6 on 2026-10-24. Nothing is fitted on labels or prices: the index's own article data stays
with the index. Exported from the tt-news-index registry (spec 1.1, registry md5 `a1607d16`) on 2026-10-24.

## Files

`0.1.0.json` the pack; `samples/inputs.json` the articles the fixture scores: Wikinews articles (CC BY 2.5, attributed in each
entry) and, for companies Wikinews rarely covers, illustrative articles written by thinkingtext (marked as such; not news reports);
`fixtures/0.1.0.json` the samples' raw results and the evaluator's output.
