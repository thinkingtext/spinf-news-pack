# thinkingtext/equity-amzn 0.1.0: the questions

Every question is the article followed by one sentence that stops where a one-word answer goes, written here as `___`. The engine
reads the two answers' log-probabilities at that point; the read is `logprob(first) − logprob(second)`, and the sign is the
direction of the first answer toward the category's "up" (a higher oil price, a higher share price). The questions are listed by
category, in the order the pack averages them.

```
<the article>

<the sentence below> ___
```

## `reflectors`: The share price, the valuation and the shareholder read

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end, and their consequence: the valuation of Amazon is likely to ___ | ` rise` / ` fall` | + | `amzn:the_valuation_of_amazon__sum` |

## `surprise`: Results and guidance against expectations

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| Summary of the key facts in the article above, from beginning to end: relative to market expectations, Amazon's quarterly results came in ___ | ` higher` / ` lower` | + | `amznrep:amazon_s_quarterly_results__sum` |
| Summary of the key facts in the article above, from beginning to end: relative to market expectations, Amazon's revenue guidance came in ___ | ` higher` / ` lower` | + | `amznrep:amazon_s_revenue_guidance__sum` |
| Summary of the key facts in the article above, from beginning to end: relative to market expectations, AWS revenue growth came in ___ | ` higher` / ` lower` | + | `amznrep:aws_revenue_growth__sum` |

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

## `company`: Amazon news read

A composite: the mean of `macro` (+), `market` (+), `reflectors` (+), `surprise` (+), each signed toward the composite's "up".
