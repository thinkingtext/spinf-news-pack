# thinkingtext/equity-aapl: Apple news

The **Apple (AAPL)** questions of Equity News Index (EQ-S10), the equity news index of thinkingtext, as a
prompt pack: the company's 15 *steady* cells, those whose daily read moved with the share price in every year of the research
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
| `demand` | Demand for the company's products and its revenue | slot | 3 |
| `profits` | Profits and margins | slot | 2 |
| `outlook` | Earnings forecasts and growth prospects | slot | 1 |
| `competition` | Market share and competitive pressure | slot | 1 |
| `reflectors` | The share price, the valuation and the shareholder read | slot | 3 |
| `surprise` | Results and guidance against expectations | slot | 1 |
| `market` | US stock and technology-stock prices, as read on the company's articles | slot | 2 |
| `macro` | Earnings, rates, risk appetite and the economy, as read on the company's articles | slot | 2 |
| `company` | Apple news read | composite | 15 |

## Cells

| cell | phrase | answers | sign | wording |
|---|---|---|---|---|
| `aapl:apple_s_revenue__sum` | Apple's revenue | rise / fall | + | summary |
| `aapl:demand_for_apple_s_products__sum` | demand for Apple's products | increase / decrease | + | summary |
| `aapl:iphone_sales__sum` | iPhone sales | increase / decrease | + | summary |
| `aapl:apple_s_profit_margins__sum` | Apple's profit margins | rise / fall | + | summary |
| `aapl:apple_s_profits__sum` | Apple's profits | rise / fall | + | summary |
| `aapl:apple_s_growth_prospects__sum` | Apple's growth prospects | improve / worsen | + | summary |
| `aapl:apple_s_market_share__sum` | Apple's market share | rise / fall | + | summary |
| `aapl:apple__sum` | Apple | positive / negative | + | sum_news_co |
| `aapl:apple_s_share_price__sum` | Apple's share price | rise / fall | + | summary |
| `aapl:the_valuation_of_apple__sum` | the valuation of Apple | rise / fall | + | summary |
| `aaplrep:apple_s_revenue_guidance__sum` | Apple's revenue guidance | higher / lower | + | sum_expect |
| `stocks:us_stock_prices__sum` | US stock prices | rise / fall | + | summary |
| `stocks:us_technology_stocks__sum` | US technology stocks | rise / fall | + | summary |
| `earnings:us_corporate_earnings__sum` | US corporate earnings | rise / fall | + | summary |
| `usa:the_risk_of_a_us_recession__sum` | the risk of a US recession | rise / fall | − | summary |

Wordings: `default` = *"{article}\n\nAs a result, {phrase} is likely to"*; `summary` = *"{article}\n\nSummary of the key facts in the
article above, from beginning to end, and their consequence: {phrase} is likely to"*; `sum_news_co` = *"... for {company} shareholders,
this news is"* (positive / negative); `sum_expect` = *"... relative to market expectations, {phrase} came in"* (higher / lower).
The sign is the direction of the first answer toward the category's "up" (a higher oil price, a higher share price).

## The index formula

EQ-S10 for Apple = 0.67 × the company read (`company`: the mean of the non-empty slot families on the day's articles) + 0.33 × the general market read (`thinkingtext/market`), each a trailing robust z; the state words are very negative, negative, balanced, positive, very positive.

## Calibration

Standardised on 1500 Wikinews business, economy, energy and company articles (CC BY 2.5; `calibration/wikinews_business.json.gz`),
scored on fp_51319d2ff6 on 2026-10-24. Nothing is fitted on labels or prices: the index's own article data stays
with the index. Exported from the tt-news-index registry (spec 1.2, registry md5 `69f13e0b`) on 2026-10-24.

## Files

`0.1.0.json` the pack; `samples/inputs.json` the articles the fixture scores: Wikinews articles (CC BY 2.5, attributed in each
entry) and, for companies Wikinews rarely covers, illustrative articles written by thinkingtext (marked as such; not news reports);
`fixtures/0.1.0.json` the samples' raw results and the evaluator's output.
