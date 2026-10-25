# thinkingtext/equity-meta 0.1.0: the questions

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
| Summary of the key facts in the article above, from beginning to end, and their consequence: demand for Meta's products is likely to ___ | ` increase` / ` decrease` | + | `meta:demand_for_meta_s_products__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: Meta's advertising revenue is likely to ___ | ` rise` / ` fall` | + | `meta:meta_s_advertising_revenue__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: Meta's revenue is likely to ___ | ` rise` / ` fall` | + | `meta:meta_s_revenue__sum` |

## `profits`: Profits and margins

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: Meta's profit margins is likely to ___ | ` rise` / ` fall` | + | `meta:meta_s_profit_margins__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: Meta's profits is likely to ___ | ` rise` / ` fall` | + | `meta:meta_s_profits__sum` |

## `outlook`: Earnings forecasts and growth prospects

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: Meta's earnings forecasts is likely to ___ | ` rise` / ` fall` | + | `meta:meta_s_earnings_forecasts__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: Meta's growth prospects is likely to ___ | ` improve` / ` worsen` | + | `meta:meta_s_growth_prospects__sum` |

## `competition`: Market share and competitive pressure

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: Meta's market share is likely to ___ | ` rise` / ` fall` | + | `meta:meta_s_market_share__sum` |

## `costs`: Costs

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: Meta's costs is likely to ___ | ` rise` / ` fall` | − | `meta:meta_s_costs__sum` |

## `reflectors`: The share price, the valuation and the shareholder read

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: for Meta shareholders, this news is ___ | ` positive` / ` negative` | + | `meta:meta__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: Meta's share price is likely to ___ | ` rise` / ` fall` | + | `meta:meta_s_share_price__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: the valuation of Meta is likely to ___ | ` rise` / ` fall` | + | `meta:the_valuation_of_meta__sum` |

## `surprise`: Results and guidance against expectations

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end: relative to market expectations, Meta's daily active users came in ___ | ` higher` / ` lower` | + | `metarep:meta_s_daily_active_users__sum` |
| Summary of the key facts in the article above, from beginning to end: relative to market expectations, Meta's quarterly results came in ___ | ` higher` / ` lower` | + | `metarep:meta_s_quarterly_results__sum` |
| Summary of the key facts in the article above, from beginning to end: relative to market expectations, Meta's revenue guidance came in ___ | ` higher` / ` lower` | + | `metarep:meta_s_revenue_guidance__sum` |

## `market`: US stock and technology-stock prices, as read on the company's articles

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: US stock prices is likely to ___ | ` rise` / ` fall` | + | `stocks:us_stock_prices__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: US technology stocks is likely to ___ | ` rise` / ` fall` | + | `stocks:us_technology_stocks__sum` |

## `macro`: Earnings, rates, risk appetite and the economy, as read on the company's articles

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: US corporate earnings is likely to ___ | ` rise` / ` fall` | + | `earnings:us_corporate_earnings__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: for investors, this news is ___ | ` positive` / ` negative` | + | `investors:news_inv_investors__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: big tech earnings is likely to ___ | ` rise` / ` fall` | + | `tech:big_tech_earnings__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: the risk of a US recession is likely to ___ | ` rise` / ` fall` | − | `usa:the_risk_of_a_us_recession__sum` |

## `company`: Meta news read

A composite: the mean of `competition` (+), `costs` (+), `demand` (+), `macro` (+), `market` (+), `outlook` (+), `profits` (+), `reflectors` (+), `surprise` (+), each signed toward the composite's "up".
