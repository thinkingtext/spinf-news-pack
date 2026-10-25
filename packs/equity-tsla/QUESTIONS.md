# thinkingtext/equity-tsla 0.1.0: the questions

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
| Summary of the key facts in the article above, from beginning to end, and their consequence: sales of electric vehicles is likely to ___ | ` increase` / ` decrease` | + | `ev:sales_of_electric_vehicles__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: demand for Tesla's products is likely to ___ | ` increase` / ` decrease` | + | `tsla:demand_for_tesla_s_products__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: Tesla's revenue is likely to ___ | ` rise` / ` fall` | + | `tsla:tesla_s_revenue__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: Tesla's vehicle deliveries is likely to ___ | ` increase` / ` decrease` | + | `tsla:tesla_s_vehicle_deliveries__sum` |

## `profits`: Profits and margins

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: Tesla's profit margins is likely to ___ | ` rise` / ` fall` | + | `tsla:tesla_s_profit_margins__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: Tesla's profits is likely to ___ | ` rise` / ` fall` | + | `tsla:tesla_s_profits__sum` |

## `outlook`: Earnings forecasts and growth prospects

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: Tesla's earnings forecasts is likely to ___ | ` rise` / ` fall` | + | `tsla:tesla_s_earnings_forecasts__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: Tesla's growth prospects is likely to ___ | ` improve` / ` worsen` | + | `tsla:tesla_s_growth_prospects__sum` |

## `competition`: Market share and competitive pressure

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: competitive pressure on Tesla is likely to ___ | ` increase` / ` decrease` | − | `tsla:competitive_pressure_on_tesla__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: Tesla's market share is likely to ___ | ` rise` / ` fall` | + | `tsla:tesla_s_market_share__sum` |

## `regulation`: Regulatory, legal and policy pressure

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: regulatory pressure on Tesla is likely to ___ | ` increase` / ` decrease` | − | `tsla:regulatory_pressure_on_tesla__sum` |

## `costs`: Costs

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: Tesla's costs is likely to ___ | ` rise` / ` fall` | − | `tsla:tesla_s_costs__sum` |

## `reflectors`: The share price, the valuation and the shareholder read

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: for Tesla shareholders, this news is ___ | ` positive` / ` negative` | + | `tsla:tesla__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: Tesla's share price is likely to ___ | ` rise` / ` fall` | + | `tsla:tesla_s_share_price__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: the valuation of Tesla is likely to ___ | ` rise` / ` fall` | + | `tsla:the_valuation_of_tesla__sum` |

## `surprise`: Results and guidance against expectations

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end: relative to market expectations, Tesla's quarterly results came in ___ | ` higher` / ` lower` | + | `tslarep:tesla_s_quarterly_results__sum` |
| Summary of the key facts in the article above, from beginning to end: relative to market expectations, Tesla's quarterly vehicle deliveries came in ___ | ` higher` / ` lower` | + | `tslarep:tesla_s_quarterly_vehicle_deliveries__sum` |
| Summary of the key facts in the article above, from beginning to end: relative to market expectations, Tesla's revenue guidance came in ___ | ` higher` / ` lower` | + | `tslarep:tesla_s_revenue_guidance__sum` |

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
| Summary of the key facts in the article above, from beginning to end, and their consequence: investor risk appetite is likely to ___ | ` improve` / ` worsen` | + | `funds:investor_risk_appetite__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: for investors, this news is ___ | ` positive` / ` negative` | + | `investors:news_inv_investors__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: big tech earnings is likely to ___ | ` rise` / ` fall` | + | `tech:big_tech_earnings__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: the risk of a US recession is likely to ___ | ` rise` / ` fall` | − | `usa:the_risk_of_a_us_recession__sum` |

## `company`: Tesla news read

A composite: the mean of `competition` (+), `costs` (+), `demand` (+), `macro` (+), `market` (+), `outlook` (+), `profits` (+), `reflectors` (+), `regulation` (+), `surprise` (+), each signed toward the composite's "up".
