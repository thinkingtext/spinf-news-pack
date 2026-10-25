# thinkingtext/equity-aapl 0.1.0: the questions

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
| Summary of the key facts in the article above, from beginning to end, and their consequence: Apple's revenue is likely to ___ | ` rise` / ` fall` | + | `aapl:apple_s_revenue__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: demand for Apple's products is likely to ___ | ` increase` / ` decrease` | + | `aapl:demand_for_apple_s_products__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: iPhone sales is likely to ___ | ` increase` / ` decrease` | + | `aapl:iphone_sales__sum` |

## `profits`: Profits and margins

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: Apple's profit margins is likely to ___ | ` rise` / ` fall` | + | `aapl:apple_s_profit_margins__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: Apple's profits is likely to ___ | ` rise` / ` fall` | + | `aapl:apple_s_profits__sum` |

## `outlook`: Earnings forecasts and growth prospects

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: Apple's growth prospects is likely to ___ | ` improve` / ` worsen` | + | `aapl:apple_s_growth_prospects__sum` |

## `competition`: Market share and competitive pressure

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: Apple's market share is likely to ___ | ` rise` / ` fall` | + | `aapl:apple_s_market_share__sum` |

## `reflectors`: The share price, the valuation and the shareholder read

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: for Apple shareholders, this news is ___ | ` positive` / ` negative` | + | `aapl:apple__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: Apple's share price is likely to ___ | ` rise` / ` fall` | + | `aapl:apple_s_share_price__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: the valuation of Apple is likely to ___ | ` rise` / ` fall` | + | `aapl:the_valuation_of_apple__sum` |

## `surprise`: Results and guidance against expectations

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end: relative to market expectations, Apple's revenue guidance came in ___ | ` higher` / ` lower` | + | `aaplrep:apple_s_revenue_guidance__sum` |

## `market`: US stock and technology-stock prices, as read on the company's articles

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: US stock prices is likely to ___ | ` rise` / ` fall` | + | `stocks:us_stock_prices__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: US technology stocks is likely to ___ | ` rise` / ` fall` | + | `stocks:us_technology_stocks__sum` |

## `macro`: Earnings, rates, risk appetite and the economy, as read on the company's articles

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: US corporate earnings is likely to ___ | ` rise` / ` fall` | + | `earnings:us_corporate_earnings__sum` |
| Summary of the key facts in the article above, from beginning to end, and their consequence: the risk of a US recession is likely to ___ | ` rise` / ` fall` | − | `usa:the_risk_of_a_us_recession__sum` |

## `company`: Apple news read

A composite: the mean of `competition` (+), `demand` (+), `macro` (+), `market` (+), `outlook` (+), `profits` (+), `reflectors` (+), `surprise` (+), each signed toward the composite's "up".
