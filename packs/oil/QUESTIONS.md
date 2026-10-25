# thinkingtext/oil 0.1.0: the questions

Every question is the article followed by one sentence that stops where a one-word answer goes, written here as `___`. The engine
reads the two answers' log-probabilities at that point; the read is `logprob(first) − logprob(second)`, and the sign is the
direction of the first answer toward the category's "up" (a higher oil price, a higher share price). The questions are listed by
category, in the order the pack averages them.

```
<the article>

<the sentence below> ___
```

## `demand`: Global oil demand

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| As a result, global oil demand is likely to ___ | ` increase` / ` decrease` | + | `world:global_oil_demand` |
| As a result, US oil demand is likely to ___ | ` increase` / ` decrease` | + | `usa:us_oil_demand` |
| As a result, Chinese oil demand is likely to ___ | ` increase` / ` decrease` | + | `china:chinese_oil_demand` |

## `supply`: Global oil supply

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| As a result, global oil supply is likely to ___ | ` increase` / ` decrease` | + | `world:global_oil_supply` |
| As a result, OPEC+ crude oil production is likely to ___ | ` increase` / ` decrease` | + | `opec:opec_crude_oil_production` |
| As a result, US shale oil production is likely to ___ | ` increase` / ` decrease` | + | `shale:us_shale_oil_production` |
| As a result, non-OPEC oil supply is likely to ___ | ` increase` / ` decrease` | + | `nonopec:non_opec_oil_supply` |

## `inventories`: US oil inventories

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| As a result, US crude oil inventories is likely to ___ | ` rise` / ` fall` | + | `us:us_crude_oil_inventories` |
| As a result, crude oil inventories at Cushing, Oklahoma is likely to ___ | ` rise` / ` fall` | + | `cushing:crude_oil_inventories_at_cushing_oklahom` |
| As a result, US gasoline inventories is likely to ___ | ` rise` / ` fall` | + | `gasoline:us_gasoline_inventories` |
| As a result, US distillate inventories is likely to ___ | ` rise` / ` fall` | + | `diesel:us_distillate_inventories` |

## `opec`: OPEC+ production quotas

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| As a result, OPEC+ production quotas is likely to ___ | ` tighten` / ` ease` | + | `opec:opec_production_quotas` |

## `disruption`: The risk of oil supply disruptions

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| As a result, the risk of oil supply disruptions in the Middle East is likely to ___ | ` rise` / ` fall` | + | `mideast:the_risk_of_oil_supply_disruptions_in_th` |
| As a result, the risk of a closure of the Strait of Hormuz is likely to ___ | ` rise` / ` fall` | + | `hormuz:the_risk_of_a_closure_of_the_strait_of_h` |
| As a result, the risk of disruption to Russian oil exports is likely to ___ | ` rise` / ` fall` | + | `russia:the_risk_of_disruption_to_russian_oil_ex` |
| As a result, the risk of escalation in the war in Ukraine is likely to ___ | ` rise` / ` fall` | + | `ukraine:the_risk_of_escalation_in_the_war_in_ukr` |

## `growth`: The global economy

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| As a result, global economic growth is likely to ___ | ` rise` / ` fall` | + | `world:global_economic_growth` |
| As a result, US economic growth is likely to ___ | ` rise` / ` fall` | + | `usa:us_economic_growth` |
| As a result, China's economic growth is likely to ___ | ` rise` / ` fall` | + | `china:china_s_economic_growth` |
| As a result, the risk of a global recession is likely to ___ | ` rise` / ` fall` | − | `world:the_risk_of_a_global_recession` |

## `rates`: US interest rates

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| As a result, US interest rates is likely to ___ | ` rise` / ` fall` | + | `fed:us_interest_rates` |
| As a result, the federal funds rate is likely to ___ | ` rise` / ` fall` | + | `fed:the_federal_funds_rate` |

## `dollar`: The US dollar

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| As a result, the US dollar is likely to ___ | ` rise` / ` fall` | + | `dollar:the_us_dollar` |
| As a result, the dollar is likely to ___ | ` strengthen` / ` weaken` | + | `dollar:the_dollar` |

## `stocks`: Stock markets

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| As a result, US stock prices is likely to ___ | ` rise` / ` fall` | + | `stocks:us_stock_prices` |
| As a result, the risk of a global recession is likely to ___ | ` rise` / ` fall` | − | `world:the_risk_of_a_global_recession` |

## `mood`: Investor sentiment

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| The mood in financial markets is one of ___ | ` optimism` / ` pessimism` | + | `market:mood_financial_markets` |
| As a result, fear in financial markets is likely to ___ | ` rise` / ` fall` | − | `market:fear_in_financial_markets` |
| As a result, investor optimism is likely to ___ | ` rise` / ` fall` | + | `market:investor_optimism` |
| As a result, risk aversion among investors is likely to ___ | ` rise` / ` fall` | − | `market:risk_aversion_among_investors` |
| As a result, turmoil in financial markets is likely to ___ | ` rise` / ` fall` | − | `market:turmoil_in_financial_markets` |

## `margins`: Refining margins

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| As a result, global refining margins is likely to ___ | ` rise` / ` fall` | + | `refiners:global_refining_margins` |
| As a result, diesel prices is likely to ___ | ` rise` / ` fall` | + | `diesel:diesel_prices` |

## `inflation`: US inflation

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| As a result, US inflation is likely to ___ | ` rise` / ` fall` | + | `fed:us_inflation` |

## `fedcuts`: Expectations of Federal Reserve rate cuts

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| As a result, expectations of Fed rate cuts is likely to ___ | ` rise` / ` fall` | + | `fed:expectations_of_fed_rate_cuts` |
| As a result, bets on Federal Reserve rate cuts is likely to ___ | ` increase` / ` decrease` | + | `fed:bets_on_federal_reserve_rate_cuts` |

## `gold`: Gold prices

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| As a result, gold prices is likely to ___ | ` rise` / ` fall` | + | `gold:gold_prices` |

## `euro`: The euro against the dollar

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| As a result, the euro against the US dollar is likely to ___ | ` rise` / ` fall` | + | `euro:the_euro_against_the_us_dollar` |
| As a result, the euro is likely to ___ | ` strengthen` / ` weaken` | + | `euro:the_euro` |

## `geopolitics`: Geopolitical tensions

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| As a result, geopolitical tensions is likely to ___ | ` ease` / ` escalate` | − | `market:geopolitical_tensions` |
| As a result, the risk of a wider war is likely to ___ | ` rise` / ` fall` | + | `market:the_risk_of_a_wider_war` |

## `trade`: Trade tensions

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| As a result, trade tensions is likely to ___ | ` ease` / ` escalate` | − | `market:trade_tensions` |
| As a result, US-China trade tensions is likely to ___ | ` rise` / ` fall` | − | `trade:us_china_trade_tensions` |

## `volatility`: Financial market volatility

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| As a result, financial market volatility is likely to ___ | ` rise` / ` fall` | + | `haven:financial_market_volatility` |
| As a result, turmoil in financial markets is likely to ___ | ` rise` / ` fall` | + | `market:turmoil_in_financial_markets` |

## `f6`: Oil news read (F6)

A composite: the mean of `demand` (+), `disruption` (+), `inventories` (−), `margins` (+), `opec` (+), `supply` (−), each signed toward the composite's "up".
