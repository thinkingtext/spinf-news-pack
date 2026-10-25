# thinkingtext/equity-amd 0.1.0: the questions

Every question is the article followed by one sentence that stops where a one-word answer goes, written here as `___`. The engine
reads the two answers' log-probabilities at that point; the read is `logprob(first) − logprob(second)`, and the sign is the
direction of the first answer toward the category's "up" (a higher oil price, a higher share price). The questions are listed by
category, in the order the pack averages them.

```
<the article>

<the sentence below> ___
```

## `demand`: Demand for the company's products and its revenue

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: AMD's revenue is likely to ___ | ` rise` / ` fall` | + | `amd:amd_s_revenue__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: demand for AMD's data centre chips is likely to ___ | ` increase` / ` decrease` | + | `amd:demand_for_amd_s_data_centre_chips__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: demand for AMD's products is likely to ___ | ` increase` / ` decrease` | + | `amd:demand_for_amd_s_products__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: capital spending on artificial intelligence is likely to ___ | ` increase` / ` decrease` | + | `tech:capital_spending_on_artificial_intellige__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: demand for AI chips is likely to ___ | ` increase` / ` decrease` | + | `tech:demand_for_ai_chips__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: semiconductor demand is likely to ___ | ` increase` / ` decrease` | + | `tech:semiconductor_demand__sum` |

## `profits`: Profits and margins

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: AMD's profit margins is likely to ___ | ` rise` / ` fall` | + | `amd:amd_s_profit_margins__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: AMD's profits is likely to ___ | ` rise` / ` fall` | + | `amd:amd_s_profits__sum` |

## `outlook`: Earnings forecasts and growth prospects

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: AMD's earnings forecasts is likely to ___ | ` rise` / ` fall` | + | `amd:amd_s_earnings_forecasts__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: AMD's growth prospects is likely to ___ | ` improve` / ` worsen` | + | `amd:amd_s_growth_prospects__sum` |

## `competition`: Market share and competitive pressure

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: AMD's market share is likely to ___ | ` rise` / ` fall` | + | `amd:amd_s_market_share__sum` |

## `reflectors`: The share price, the valuation and the shareholder read

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: for AMD shareholders, this news is ___ | ` positive` / ` negative` | + | `amd:amd__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: AMD's share price is likely to ___ | ` rise` / ` fall` | + | `amd:amd_s_share_price__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: the valuation of AMD is likely to ___ | ` rise` / ` fall` | + | `amd:the_valuation_of_amd__sum` |

## `surprise`: Results and guidance against expectations

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end: relative to market expectations, AMD's data centre revenue came in ___ | ` higher` / ` lower` | + | `amdrep:amd_s_data_centre_revenue__sum` |
| Summary of the key facts in the article above, from beginning to end: relative to market expectations, AMD's quarterly results came in ___ | ` higher` / ` lower` | + | `amdrep:amd_s_quarterly_results__sum` |
| Summary of the key facts in the article above, from beginning to end: relative to market expectations, AMD's revenue guidance came in ___ | ` higher` / ` lower` | + | `amdrep:amd_s_revenue_guidance__sum` |

## `market`: US stock and technology-stock prices, as read on the company's articles

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: US stock prices is likely to ___ | ` rise` / ` fall` | + | `stocks:us_stock_prices__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: US technology stocks is likely to ___ | ` rise` / ` fall` | + | `stocks:us_technology_stocks__sum` |

## `macro`: Earnings, rates, risk appetite and the economy, as read on the company's articles

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: US corporate earnings is likely to ___ | ` rise` / ` fall` | + | `earnings:us_corporate_earnings__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: expectations of Fed rate cuts is likely to ___ | ` rise` / ` fall` | + | `fed:expectations_of_fed_rate_cuts__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: financial market volatility is likely to ___ | ` rise` / ` fall` | − | `haven:financial_market_volatility__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: for investors, this news is ___ | ` positive` / ` negative` | + | `investors:news_inv_investors__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: the risk of a US recession is likely to ___ | ` rise` / ` fall` | − | `usa:the_risk_of_a_us_recession__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: US tariffs on imports is likely to ___ | ` tighten` / ` ease` | − | `uspolicy:us_tariffs_on_imports__sum` |

## `company`: AMD news read

A composite: the mean of `competition` (+), `demand` (+), `macro` (+), `market` (+), `outlook` (+), `profits` (+), `reflectors` (+), `surprise` (+), each signed toward the composite's "up".
