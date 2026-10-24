# thinkingtext/equity-pltr: Palantir news

The **Palantir (PLTR)** questions of Equity News Index (EQ-S10), the equity news index of thinkingtext, as a
prompt pack: the company's 21 *steady* cells, those whose daily read moved with the share price in every year of the research
window, by slot family, read on an article about the company. The reads are whole-article wordings ("Summary of the key facts in
the article above, from beginning to end, and their consequence: ... is likely to") with two single-token answers of opposite
direction; each is signed toward a **higher share price**.

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

| id | family | role | cells |
|---|---|---|---|
| `demand` | Demand for the company's products and its revenue | slot | 2 |
| `profits` | Profits and margins | slot | 2 |
| `outlook` | Earnings forecasts and growth prospects | slot | 2 |
| `competition` | Market share and competitive pressure | slot | 2 |
| `reflectors` | The share price, the valuation and the shareholder read | slot | 3 |
| `surprise` | Results and guidance against expectations | slot | 3 |
| `market` | US stock and technology-stock prices, as read on the company's articles | slot | 2 |
| `macro` | Earnings, rates, risk appetite and the economy, as read on the company's articles | slot | 5 |
| `company` | Palantir news read | composite | 21 |

## Cells

| cell | phrase | answers | sign | wording |
|---|---|---|---|---|
| `pltr:demand_for_palantir_s_products__sum` | demand for Palantir's products | increase / decrease | + | summary |
| `pltr:palantir_s_revenue__sum` | Palantir's revenue | rise / fall | + | summary |
| `pltr:palantir_s_profit_margins__sum` | Palantir's profit margins | rise / fall | + | summary |
| `pltr:palantir_s_profits__sum` | Palantir's profits | rise / fall | + | summary |
| `pltr:palantir_s_earnings_forecasts__sum` | Palantir's earnings forecasts | rise / fall | + | summary |
| `pltr:palantir_s_growth_prospects__sum` | Palantir's growth prospects | improve / worsen | + | summary |
| `pltr:competitive_pressure_on_palantir__sum` | competitive pressure on Palantir | increase / decrease | − | summary |
| `pltr:palantir_s_market_share__sum` | Palantir's market share | rise / fall | + | summary |
| `pltr:palantir__sum` | Palantir | positive / negative | + | sum_news_co |
| `pltr:palantir_s_share_price__sum` | Palantir's share price | rise / fall | + | summary |
| `pltr:the_valuation_of_palantir__sum` | the valuation of Palantir | rise / fall | + | summary |
| `pltrrep:palantir_s_quarterly_results__sum` | Palantir's quarterly results | higher / lower | + | sum_expect |
| `pltrrep:palantir_s_revenue_guidance__sum` | Palantir's revenue guidance | higher / lower | + | sum_expect |
| `pltrrep:palantir_s_us_commercial_revenue__sum` | Palantir's US commercial revenue | higher / lower | + | sum_expect |
| `stocks:us_stock_prices__sum` | US stock prices | rise / fall | + | summary |
| `stocks:us_technology_stocks__sum` | US technology stocks | rise / fall | + | summary |
| `earnings:us_corporate_earnings__sum` | US corporate earnings | rise / fall | + | summary |
| `fed:expectations_of_fed_rate_cuts__sum` | expectations of Fed rate cuts | rise / fall | + | summary |
| `haven:financial_market_volatility__sum` | financial market volatility | rise / fall | − | summary |
| `investors:news_inv_investors__sum` | investors | positive / negative | + | sum_news_inv |
| `usa:us_economic_growth__sum` | US economic growth | rise / fall | + | summary |

Wordings: `default` = *"{article}\n\nAs a result, {phrase} is likely to"*; `summary` = *"{article}\n\nSummary of the key facts in the
article above, from beginning to end, and their consequence: {phrase} is likely to"*; `sum_news_co` = *"... for {company} shareholders,
this news is"* (positive / negative); `sum_expect` = *"... relative to market expectations, {phrase} came in"* (higher / lower).
The sign is the direction of the first answer toward the category's "up" (a higher oil price, a higher share price).

## The index formula

EQ-S10 for Palantir = 0.67 × the company read (`company`: the mean of the non-empty slot families on the day's articles) + 0.33 × the general market read (`thinkingtext/market`), each a trailing robust z; the state words are very negative, negative, balanced, positive, very positive.

## Calibration

Standardised on 1500 Wikinews business, economy, energy and company articles (CC BY 2.5; `calibration/wikinews_business.json.gz`),
scored on fp_51319d2ff6 on 2026-10-24. Nothing is fitted on labels or prices: the index's own article data stays
with the index. Exported from the tt-news-index registry (spec 1.2, registry md5 `85a42031`) on 2026-10-24.

## Files

`0.1.0.json` the pack; `samples/inputs.json` the articles the fixture scores: Wikinews articles (CC BY 2.5, attributed in each
entry) and, for companies Wikinews rarely covers, illustrative articles written by thinkingtext (marked as such; not news reports);
`fixtures/0.1.0.json` the samples' raw results and the evaluator's output.
