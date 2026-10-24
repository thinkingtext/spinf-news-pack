# thinkingtext/market: Market news

The **general market read** of Equity News Index (EQ-S10), the equity news index of thinkingtext, as a prompt pack: 126 macro
and market cells (growth, rates, inflation, earnings, risk appetite, currencies, commodities, trade), each signed toward higher US
stock prices, read on business news. In the index this read is one third of every company's index and is published on its own
against the Nasdaq-100.

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
| `market` | General market read | composite | 126 |

## Cells

| cell | phrase | answers | sign | wording |
|---|---|---|---|---|
| `asia:asian_oil_demand` | Asian oil demand | increase / decrease | + | default |
| `australia:australia_s_economic_growth` | Australia's economic growth | rise / fall | + | default |
| `australia:australian_commodity_exports` | Australian commodity exports | increase / decrease | + | default |
| `australia:australian_consumer_spending` | Australian consumer spending | increase / decrease | + | default |
| `australia:australian_iron_ore_exports` | Australian iron ore exports | increase / decrease | + | default |
| `australia:the_australian_dollar` | the Australian dollar | strengthen / weaken | + | default |
| `australia:the_australian_dollar_against_the_us_dol` | the Australian dollar against the US dollar | rise / fall | + | default |
| `autos:european_car_sales` | European car sales | increase / decrease | + | default |
| `banks:european_bank_earnings` | European bank earnings | rise / fall | + | default |
| `banks:us_bank_lending` | US bank lending | increase / decrease | + | default |
| `boe:uk_inflation` | UK inflation | rise / fall | − | default |
| `cad:canada_s_economic_growth` | Canada's economic growth | rise / fall | + | default |
| `cad:the_canadian_dollar` | the Canadian dollar | strengthen / weaken | + | default |
| `china:china_s_economic_growth` | China's economic growth | rise / fall | + | default |
| `china:china_s_property_market` | China's property market | improve / worsen | + | default |
| `china:chinese_consumer_spending` | Chinese consumer spending | increase / decrease | + | default |
| `china:chinese_holdings_of_us_treasuries` | Chinese holdings of US Treasuries | rise / fall | + | default |
| `credit:us_credit_spreads` | US credit spreads | widen / narrow | − | default |
| `crypto:bitcoin_prices` | Bitcoin prices | rise / fall | + | default |
| `dollar:the_canadian_dollar` | the Canadian dollar | rise / fall | + | default |
| `dollar:the_dollar` | the dollar | strengthen / weaken | − | default |
| `dollar:the_us_dollar` | the US dollar | rise / fall | − | default |
| `earnings:corporate_share_buybacks` | corporate share buybacks | increase / decrease | + | default |
| `earnings:european_corporate_earnings` | European corporate earnings | rise / fall | + | default |
| `earnings:us_corporate_earnings` | US corporate earnings | rise / fall | + | default |
| `earnings:us_corporate_earnings_forecasts` | US corporate earnings forecasts | rise / fall | + | default |
| `ecb:eurozone_manufacturing_activity` | eurozone manufacturing activity | expand / contract | + | default |
| `euro:the_euro` | the euro | strengthen / weaken | + | default |
| `euro:the_euro_against_the_us_dollar` | the euro against the US dollar | rise / fall | + | default |
| `europe:european_economic_growth` | European economic growth | rise / fall | + | default |
| `europe:european_manufacturing_activity` | European manufacturing activity | expand / contract | + | default |
| `europe:european_oil_demand` | European oil demand | increase / decrease | + | default |
| `eustocks:european_stock_prices` | European stock prices | rise / fall | + | default |
| `eustocks:the_dax` | the DAX | rise / fall | + | default |
| `eustocks:the_stoxx_600` | the Stoxx 600 | rise / fall | + | default |
| `fed:expectations_of_fed_rate_cuts` | expectations of Fed rate cuts | rise / fall | + | default |
| `fed:the_federal_funds_rate` | the federal funds rate | rise / fall | − | default |
| `fed:the_federal_reserve` | the Federal Reserve | cut / raise | + | default |
| `fed:us_inflation` | US inflation | rise / fall | − | default |
| `fed:us_interest_rates` | US interest rates | rise / fall | − | default |
| `fed:us_monetary_policy` | US monetary policy | tighten / ease | − | default |
| `fedind:political_pressure_on_the_federal_reserv` | political pressure on the Federal Reserve | increase / decrease | − | default |
| `funds:investor_risk_appetite` | investor risk appetite | improve / worsen | + | default |
| `germany:german_manufacturing_activity` | German manufacturing activity | expand / contract | + | default |
| `gold:gold_mine_production` | gold mine production | increase / decrease | + | default |
| `gold:jewellery_demand_for_gold` | jewellery demand for gold | increase / decrease | + | default |
| `haven:financial_market_volatility` | financial market volatility | rise / fall | − | default |
| `haven:safe_haven_demand` | safe-haven demand | increase / decrease | − | default |
| `household:consumer_spending` | consumer spending | increase / decrease | + | default |
| `housing:australian_house_prices` | Australian house prices | rise / fall | + | default |
| `housing:canadian_home_sales` | Canadian home sales | increase / decrease | + | default |
| `housing:new_zealand_house_prices` | New Zealand house prices | rise / fall | + | default |
| `housing:uk_house_prices` | UK house prices | rise / fall | + | default |
| `housing:us_home_sales` | US home sales | increase / decrease | + | default |
| `housing:us_mortgage_rates` | US mortgage rates | rise / fall | − | default |
| `india:indian_gold_demand` | Indian gold demand | increase / decrease | + | default |
| `india:indian_gold_imports` | Indian gold imports | increase / decrease | + | default |
| `ironore:chinese_demand_for_iron_ore` | Chinese demand for iron ore | increase / decrease | + | default |
| `ironore:iron_ore_prices` | iron ore prices | rise / fall | + | default |
| `japan:foreign_investment_in_japanese_stocks` | foreign investment in Japanese stocks | increase / decrease | + | default |
| `japan:japan_s_economic_growth` | Japan's economic growth | rise / fall | + | default |
| `japan:japanese_car_exports_to_the_united_state` | Japanese car exports to the United States | increase / decrease | + | default |
| `japan:japanese_corporate_earnings` | Japanese corporate earnings | rise / fall | + | default |
| `japan:japanese_exports` | Japanese exports | increase / decrease | + | default |
| `japan:japanese_inflation` | Japanese inflation | rise / fall | − | default |
| `japan:japanese_investors_demand_for_us_treasur` | Japanese investors' demand for US Treasuries | increase / decrease | + | default |
| `japan:japanese_share_buybacks` | Japanese share buybacks | increase / decrease | + | default |
| `japan:the_nikkei` | the Nikkei | rise / fall | + | default |
| `luxury:luxury_goods_demand_in_china` | luxury goods demand in China | increase / decrease | + | default |
| `nz:new_zealand_s_economic_growth` | New Zealand's economic growth | rise / fall | + | default |
| `nz:the_new_zealand_dollar` | the New Zealand dollar | strengthen / weaken | + | default |
| `nz:the_new_zealand_dollar_against_the_us_do` | the New Zealand dollar against the US dollar | rise / fall | + | default |
| `rba:the_reserve_bank_of_australia` | the Reserve Bank of Australia | cut / raise | + | default |
| `rbnz:new_zealand_inflation` | New Zealand inflation | rise / fall | − | default |
| `rbnz:the_reserve_bank_of_new_zealand` | the Reserve Bank of New Zealand | cut / raise | + | default |
| `redsea:the_risk_of_attacks_on_shipping_in_the_r` | the risk of attacks on shipping in the Red Sea | rise / fall | − | default |
| `silver:silver_prices` | silver prices | rise / fall | + | default |
| `smallcap:us_regional_bank_earnings` | US regional bank earnings | rise / fall | + | default |
| `smallcap:us_small_business_confidence` | US small business confidence | rise / fall | + | default |
| `smallcap:us_small_cap_stocks` | US small-cap stocks | rise / fall | + | default |
| `snb:swiss_inflation` | Swiss inflation | rise / fall | − | default |
| `snb:the_swiss_national_bank` | the Swiss National Bank | cut / raise | + | default |
| `stocks:the_s_p_500` | the S&P 500 | rise / fall | + | default |
| `stocks:us_stock_prices` | US stock prices | rise / fall | + | default |
| `stocks:us_technology_stocks` | US technology stocks | rise / fall | + | default |
| `swiss:swiss_exports` | Swiss exports | increase / decrease | + | default |
| `swiss:swiss_pharmaceutical_exports` | Swiss pharmaceutical exports | increase / decrease | + | default |
| `swiss:switzerland_s_economic_growth` | Switzerland's economic growth | rise / fall | + | default |
| `swiss:the_swiss_franc` | the Swiss franc | strengthen / weaken | − | default |
| `taiwan:the_risk_of_a_conflict_between_china_and` | the risk of a conflict between China and Taiwan | rise / fall | − | default |
| `tech:big_tech_earnings` | big tech earnings | rise / fall | + | default |
| `tech:capital_spending_on_artificial_intellige` | capital spending on artificial intelligence | increase / decrease | + | default |
| `tech:demand_for_ai_chips` | demand for AI chips | increase / decrease | + | default |
| `tech:semiconductor_demand` | semiconductor demand | increase / decrease | + | default |
| `treasury:10_year_us_treasury_yields` | 10-year US Treasury yields | rise / fall | − | default |
| `treasury:2_year_us_treasury_yields` | 2-year US Treasury yields | rise / fall | − | default |
| `treasury:30_year_us_treasury_yields` | 30-year US Treasury yields | rise / fall | − | default |
| `treasury:the_us_treasury_term_premium` | the US Treasury term premium | rise / fall | − | default |
| `treasury:us_bond_market_volatility` | US bond market volatility | rise / fall | − | default |
| `treasury:us_real_yields` | US real yields | rise / fall | − | default |
| `treasury:us_treasury_yields` | US Treasury yields | rise / fall | − | default |
| `uk:sterling_against_the_us_dollar` | sterling against the US dollar | rise / fall | + | default |
| `uk:the_pound` | the pound | strengthen / weaken | + | default |
| `uk:the_uk_unemployment_rate` | the UK unemployment rate | rise / fall | − | default |
| `uk:uk_economic_growth` | UK economic growth | rise / fall | + | default |
| `uk:uk_eu_trade_relations` | UK-EU trade relations | improve / worsen | + | default |
| `uk:uk_public_finances` | UK public finances | improve / worsen | + | default |
| `uk:uk_retail_sales` | UK retail sales | rise / fall | + | default |
| `uk:uk_services_activity` | UK services activity | expand / contract | + | default |
| `usa:consumer_confidence` | consumer confidence | rise / fall | + | default |
| `usa:the_risk_of_a_us_recession` | the risk of a US recession | rise / fall | − | default |
| `usa:us_business_investment` | US business investment | increase / decrease | + | default |
| `usa:us_economic_growth` | US economic growth | rise / fall | + | default |
| `usa:us_manufacturing_activity` | US manufacturing activity | expand / contract | + | default |
| `usa:us_oil_demand` | US oil demand | increase / decrease | + | default |
| `usa:us_retail_sales` | US retail sales | rise / fall | + | default |
| `usa:us_services_activity` | US services activity | expand / contract | + | default |
| `usdata:the_us_cpi_inflation_print` | the US CPI inflation print | higher / lower | − | expect |
| `usfiscal:the_risk_of_a_us_government_shutdown` | the risk of a US government shutdown | rise / fall | − | default |
| `usjobs:the_us_labour_market` | the US labour market | improve / worsen | + | default |
| `usjobs:us_layoffs` | US layoffs | increase / decrease | − | default |
| `uspolicy:us_export_controls_on_semiconductors` | US export controls on semiconductors | tighten / ease | − | default |
| `uspolicy:us_tariffs_on_imports` | US tariffs on imports | tighten / ease | − | default |
| `world:global_economic_growth` | global economic growth | rise / fall | + | default |
| `world:global_oil_demand` | global oil demand | increase / decrease | + | default |
| `world:the_risk_of_a_global_recession` | the risk of a global recession | rise / fall | − | default |

Wordings: `default` = *"{article}\n\nAs a result, {phrase} is likely to"*; `summary` = *"{article}\n\nSummary of the key facts in the
article above, from beginning to end, and their consequence: {phrase} is likely to"*; `sum_news_co` = *"... for {company} shareholders,
this news is"* (positive / negative); `sum_expect` = *"... relative to market expectations, {phrase} came in"* (higher / lower).
The sign is the direction of the first answer toward the category's "up" (a higher oil price, a higher share price).

## Calibration

Standardised on 1500 Wikinews business, economy, energy and company articles (CC BY 2.5; `calibration/wikinews_business.json.gz`),
scored on fp_51319d2ff6 on 2026-10-24. Nothing is fitted on labels or prices: the index's own article data stays
with the index. Exported from the tt-news-index registry (spec 1.2, registry md5 `c46b2b1a`) on 2026-10-24.

## Files

`0.1.0.json` the pack; `samples/inputs.json` the articles the fixture scores: Wikinews articles (CC BY 2.5, attributed in each
entry) and, for companies Wikinews rarely covers, illustrative articles written by thinkingtext (marked as such; not news reports);
`fixtures/0.1.0.json` the samples' raw results and the evaluator's output.
