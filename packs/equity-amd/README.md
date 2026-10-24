# thinkingtext/equity-amd: AMD news

The **AMD (AMD)** questions of Equity News Index (EQ-S10), the equity news index of thinkingtext, as a
prompt pack: the company's 25 *steady* cells, those whose daily read moved with the share price in every year of the research
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
| `demand` | Demand for the company's products and its revenue | slot | 6 |
| `profits` | Profits and margins | slot | 2 |
| `outlook` | Earnings forecasts and growth prospects | slot | 2 |
| `competition` | Market share and competitive pressure | slot | 1 |
| `reflectors` | The share price, the valuation and the shareholder read | slot | 3 |
| `surprise` | Results and guidance against expectations | slot | 3 |
| `market` | US stock and technology-stock prices, as read on the company's articles | slot | 2 |
| `macro` | Earnings, rates, risk appetite and the economy, as read on the company's articles | slot | 6 |
| `company` | AMD news read | composite | 25 |

## Cells

| cell | phrase | answers | sign | wording |
|---|---|---|---|---|
| `amd:amd_s_revenue__sum` | AMD's revenue | rise / fall | + | summary |
| `amd:demand_for_amd_s_data_centre_chips__sum` | demand for AMD's data centre chips | increase / decrease | + | summary |
| `amd:demand_for_amd_s_products__sum` | demand for AMD's products | increase / decrease | + | summary |
| `tech:capital_spending_on_artificial_intellige__sum` | capital spending on artificial intelligence | increase / decrease | + | summary |
| `tech:demand_for_ai_chips__sum` | demand for AI chips | increase / decrease | + | summary |
| `tech:semiconductor_demand__sum` | semiconductor demand | increase / decrease | + | summary |
| `amd:amd_s_profit_margins__sum` | AMD's profit margins | rise / fall | + | summary |
| `amd:amd_s_profits__sum` | AMD's profits | rise / fall | + | summary |
| `amd:amd_s_earnings_forecasts__sum` | AMD's earnings forecasts | rise / fall | + | summary |
| `amd:amd_s_growth_prospects__sum` | AMD's growth prospects | improve / worsen | + | summary |
| `amd:amd_s_market_share__sum` | AMD's market share | rise / fall | + | summary |
| `amd:amd__sum` | AMD | positive / negative | + | sum_news_co |
| `amd:amd_s_share_price__sum` | AMD's share price | rise / fall | + | summary |
| `amd:the_valuation_of_amd__sum` | the valuation of AMD | rise / fall | + | summary |
| `amdrep:amd_s_data_centre_revenue__sum` | AMD's data centre revenue | higher / lower | + | sum_expect |
| `amdrep:amd_s_quarterly_results__sum` | AMD's quarterly results | higher / lower | + | sum_expect |
| `amdrep:amd_s_revenue_guidance__sum` | AMD's revenue guidance | higher / lower | + | sum_expect |
| `stocks:us_stock_prices__sum` | US stock prices | rise / fall | + | summary |
| `stocks:us_technology_stocks__sum` | US technology stocks | rise / fall | + | summary |
| `earnings:us_corporate_earnings__sum` | US corporate earnings | rise / fall | + | summary |
| `fed:expectations_of_fed_rate_cuts__sum` | expectations of Fed rate cuts | rise / fall | + | summary |
| `haven:financial_market_volatility__sum` | financial market volatility | rise / fall | − | summary |
| `investors:news_inv_investors__sum` | investors | positive / negative | + | sum_news_inv |
| `usa:the_risk_of_a_us_recession__sum` | the risk of a US recession | rise / fall | − | summary |
| `uspolicy:us_tariffs_on_imports__sum` | US tariffs on imports | tighten / ease | − | summary |

Wordings: `default` = *"{article}\n\nAs a result, {phrase} is likely to"*; `summary` = *"{article}\n\nSummary of the key facts in the
article above, from beginning to end, and their consequence: {phrase} is likely to"*; `sum_news_co` = *"... for {company} shareholders,
this news is"* (positive / negative); `sum_expect` = *"... relative to market expectations, {phrase} came in"* (higher / lower).
The sign is the direction of the first answer toward the category's "up" (a higher oil price, a higher share price).

## The index formula

EQ-S10 for AMD = 0.52 × the company read (`company`: the mean of the non-empty slot families on the day's articles) + 0.15 × the peers' company reads (NVDA, INTC, MU) + 0.33 × the general market read (`thinkingtext/market`), each a trailing robust z; the state words are very negative, negative, balanced, positive, very positive.

## Calibration

Standardised on 1500 Wikinews business, economy, energy and company articles (CC BY 2.5; `calibration/wikinews_business.json.gz`),
scored on fp_51319d2ff6 on 2026-10-24. Nothing is fitted on labels or prices: the index's own article data stays
with the index. Exported from the tt-news-index registry (spec 1.2, registry md5 `1b4bc36f`) on 2026-10-24.

## Files

`0.1.0.json` the pack; `samples/inputs.json` the articles the fixture scores: Wikinews articles (CC BY 2.5, attributed in each
entry) and, for companies Wikinews rarely covers, illustrative articles written by thinkingtext (marked as such; not news reports);
`fixtures/0.1.0.json` the samples' raw results and the evaluator's output.
