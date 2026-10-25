# thinkingtext/market 0.1.0: the questions

Every question is the article followed by one sentence that stops where a one-word answer goes, written here as `___`. The engine
reads the two answers' log-probabilities at that point; the read is `logprob(first) − logprob(second)`, and the sign is the
direction of the first answer toward the category's "up" (a higher oil price, a higher share price). The questions are listed by
category, in the order the pack averages them.

```
<the article>

<the sentence below> ___
```

## `market`: General market read

| question (after the article) | answers | sign | cell |
|---|---|---|---|
| As a result, Asian oil demand is likely to ___ | ` increase` / ` decrease` | + | `asia:asian_oil_demand` |
| As a result, Australia's economic growth is likely to ___ | ` rise` / ` fall` | + | `australia:australia_s_economic_growth` |
| As a result, Australian commodity exports is likely to ___ | ` increase` / ` decrease` | + | `australia:australian_commodity_exports` |
| As a result, Australian consumer spending is likely to ___ | ` increase` / ` decrease` | + | `australia:australian_consumer_spending` |
| As a result, Australian iron ore exports is likely to ___ | ` increase` / ` decrease` | + | `australia:australian_iron_ore_exports` |
| As a result, the Australian dollar is likely to ___ | ` strengthen` / ` weaken` | + | `australia:the_australian_dollar` |
| As a result, the Australian dollar against the US dollar is likely to ___ | ` rise` / ` fall` | + | `australia:the_australian_dollar_against_the_us_dol` |
| As a result, European car sales is likely to ___ | ` increase` / ` decrease` | + | `autos:european_car_sales` |
| As a result, European bank earnings is likely to ___ | ` rise` / ` fall` | + | `banks:european_bank_earnings` |
| As a result, US bank lending is likely to ___ | ` increase` / ` decrease` | + | `banks:us_bank_lending` |
| As a result, UK inflation is likely to ___ | ` rise` / ` fall` | − | `boe:uk_inflation` |
| As a result, Canada's economic growth is likely to ___ | ` rise` / ` fall` | + | `cad:canada_s_economic_growth` |
| As a result, the Canadian dollar is likely to ___ | ` strengthen` / ` weaken` | + | `cad:the_canadian_dollar` |
| As a result, China's economic growth is likely to ___ | ` rise` / ` fall` | + | `china:china_s_economic_growth` |
| As a result, China's property market is likely to ___ | ` improve` / ` worsen` | + | `china:china_s_property_market` |
| As a result, Chinese consumer spending is likely to ___ | ` increase` / ` decrease` | + | `china:chinese_consumer_spending` |
| As a result, Chinese holdings of US Treasuries is likely to ___ | ` rise` / ` fall` | + | `china:chinese_holdings_of_us_treasuries` |
| As a result, US credit spreads is likely to ___ | ` widen` / ` narrow` | − | `credit:us_credit_spreads` |
| As a result, Bitcoin prices is likely to ___ | ` rise` / ` fall` | + | `crypto:bitcoin_prices` |
| As a result, the Canadian dollar is likely to ___ | ` rise` / ` fall` | + | `dollar:the_canadian_dollar` |
| As a result, the dollar is likely to ___ | ` strengthen` / ` weaken` | − | `dollar:the_dollar` |
| As a result, the US dollar is likely to ___ | ` rise` / ` fall` | − | `dollar:the_us_dollar` |
| As a result, corporate share buybacks is likely to ___ | ` increase` / ` decrease` | + | `earnings:corporate_share_buybacks` |
| As a result, European corporate earnings is likely to ___ | ` rise` / ` fall` | + | `earnings:european_corporate_earnings` |
| As a result, US corporate earnings is likely to ___ | ` rise` / ` fall` | + | `earnings:us_corporate_earnings` |
| As a result, US corporate earnings forecasts is likely to ___ | ` rise` / ` fall` | + | `earnings:us_corporate_earnings_forecasts` |
| As a result, eurozone manufacturing activity is likely to ___ | ` expand` / ` contract` | + | `ecb:eurozone_manufacturing_activity` |
| As a result, the euro is likely to ___ | ` strengthen` / ` weaken` | + | `euro:the_euro` |
| As a result, the euro against the US dollar is likely to ___ | ` rise` / ` fall` | + | `euro:the_euro_against_the_us_dollar` |
| As a result, European economic growth is likely to ___ | ` rise` / ` fall` | + | `europe:european_economic_growth` |
| As a result, European manufacturing activity is likely to ___ | ` expand` / ` contract` | + | `europe:european_manufacturing_activity` |
| As a result, European oil demand is likely to ___ | ` increase` / ` decrease` | + | `europe:european_oil_demand` |
| As a result, European stock prices is likely to ___ | ` rise` / ` fall` | + | `eustocks:european_stock_prices` |
| As a result, the DAX is likely to ___ | ` rise` / ` fall` | + | `eustocks:the_dax` |
| As a result, the Stoxx 600 is likely to ___ | ` rise` / ` fall` | + | `eustocks:the_stoxx_600` |
| As a result, expectations of Fed rate cuts is likely to ___ | ` rise` / ` fall` | + | `fed:expectations_of_fed_rate_cuts` |
| As a result, the federal funds rate is likely to ___ | ` rise` / ` fall` | − | `fed:the_federal_funds_rate` |
| As a result, the Federal Reserve is likely to ___ | ` cut` / ` raise` | + | `fed:the_federal_reserve` |
| As a result, US inflation is likely to ___ | ` rise` / ` fall` | − | `fed:us_inflation` |
| As a result, US interest rates is likely to ___ | ` rise` / ` fall` | − | `fed:us_interest_rates` |
| As a result, US monetary policy is likely to ___ | ` tighten` / ` ease` | − | `fed:us_monetary_policy` |
| As a result, political pressure on the Federal Reserve is likely to ___ | ` increase` / ` decrease` | − | `fedind:political_pressure_on_the_federal_reserv` |
| As a result, investor risk appetite is likely to ___ | ` improve` / ` worsen` | + | `funds:investor_risk_appetite` |
| As a result, German manufacturing activity is likely to ___ | ` expand` / ` contract` | + | `germany:german_manufacturing_activity` |
| As a result, gold mine production is likely to ___ | ` increase` / ` decrease` | + | `gold:gold_mine_production` |
| As a result, jewellery demand for gold is likely to ___ | ` increase` / ` decrease` | + | `gold:jewellery_demand_for_gold` |
| As a result, financial market volatility is likely to ___ | ` rise` / ` fall` | − | `haven:financial_market_volatility` |
| As a result, safe-haven demand is likely to ___ | ` increase` / ` decrease` | − | `haven:safe_haven_demand` |
| As a result, consumer spending is likely to ___ | ` increase` / ` decrease` | + | `household:consumer_spending` |
| As a result, Australian house prices is likely to ___ | ` rise` / ` fall` | + | `housing:australian_house_prices` |
| As a result, Canadian home sales is likely to ___ | ` increase` / ` decrease` | + | `housing:canadian_home_sales` |
| As a result, New Zealand house prices is likely to ___ | ` rise` / ` fall` | + | `housing:new_zealand_house_prices` |
| As a result, UK house prices is likely to ___ | ` rise` / ` fall` | + | `housing:uk_house_prices` |
| As a result, US home sales is likely to ___ | ` increase` / ` decrease` | + | `housing:us_home_sales` |
| As a result, US mortgage rates is likely to ___ | ` rise` / ` fall` | − | `housing:us_mortgage_rates` |
| As a result, Indian gold demand is likely to ___ | ` increase` / ` decrease` | + | `india:indian_gold_demand` |
| As a result, Indian gold imports is likely to ___ | ` increase` / ` decrease` | + | `india:indian_gold_imports` |
| As a result, Chinese demand for iron ore is likely to ___ | ` increase` / ` decrease` | + | `ironore:chinese_demand_for_iron_ore` |
| As a result, iron ore prices is likely to ___ | ` rise` / ` fall` | + | `ironore:iron_ore_prices` |
| As a result, foreign investment in Japanese stocks is likely to ___ | ` increase` / ` decrease` | + | `japan:foreign_investment_in_japanese_stocks` |
| As a result, Japan's economic growth is likely to ___ | ` rise` / ` fall` | + | `japan:japan_s_economic_growth` |
| As a result, Japanese car exports to the United States is likely to ___ | ` increase` / ` decrease` | + | `japan:japanese_car_exports_to_the_united_state` |
| As a result, Japanese corporate earnings is likely to ___ | ` rise` / ` fall` | + | `japan:japanese_corporate_earnings` |
| As a result, Japanese exports is likely to ___ | ` increase` / ` decrease` | + | `japan:japanese_exports` |
| As a result, Japanese inflation is likely to ___ | ` rise` / ` fall` | − | `japan:japanese_inflation` |
| As a result, Japanese investors' demand for US Treasuries is likely to ___ | ` increase` / ` decrease` | + | `japan:japanese_investors_demand_for_us_treasur` |
| As a result, Japanese share buybacks is likely to ___ | ` increase` / ` decrease` | + | `japan:japanese_share_buybacks` |
| As a result, the Nikkei is likely to ___ | ` rise` / ` fall` | + | `japan:the_nikkei` |
| As a result, luxury goods demand in China is likely to ___ | ` increase` / ` decrease` | + | `luxury:luxury_goods_demand_in_china` |
| As a result, New Zealand's economic growth is likely to ___ | ` rise` / ` fall` | + | `nz:new_zealand_s_economic_growth` |
| As a result, the New Zealand dollar is likely to ___ | ` strengthen` / ` weaken` | + | `nz:the_new_zealand_dollar` |
| As a result, the New Zealand dollar against the US dollar is likely to ___ | ` rise` / ` fall` | + | `nz:the_new_zealand_dollar_against_the_us_do` |
| As a result, the Reserve Bank of Australia is likely to ___ | ` cut` / ` raise` | + | `rba:the_reserve_bank_of_australia` |
| As a result, New Zealand inflation is likely to ___ | ` rise` / ` fall` | − | `rbnz:new_zealand_inflation` |
| As a result, the Reserve Bank of New Zealand is likely to ___ | ` cut` / ` raise` | + | `rbnz:the_reserve_bank_of_new_zealand` |
| As a result, the risk of attacks on shipping in the Red Sea is likely to ___ | ` rise` / ` fall` | − | `redsea:the_risk_of_attacks_on_shipping_in_the_r` |
| As a result, silver prices is likely to ___ | ` rise` / ` fall` | + | `silver:silver_prices` |
| As a result, US regional bank earnings is likely to ___ | ` rise` / ` fall` | + | `smallcap:us_regional_bank_earnings` |
| As a result, US small business confidence is likely to ___ | ` rise` / ` fall` | + | `smallcap:us_small_business_confidence` |
| As a result, US small-cap stocks is likely to ___ | ` rise` / ` fall` | + | `smallcap:us_small_cap_stocks` |
| As a result, Swiss inflation is likely to ___ | ` rise` / ` fall` | − | `snb:swiss_inflation` |
| As a result, the Swiss National Bank is likely to ___ | ` cut` / ` raise` | + | `snb:the_swiss_national_bank` |
| As a result, the S&P 500 is likely to ___ | ` rise` / ` fall` | + | `stocks:the_s_p_500` |
| As a result, US stock prices is likely to ___ | ` rise` / ` fall` | + | `stocks:us_stock_prices` |
| As a result, US technology stocks is likely to ___ | ` rise` / ` fall` | + | `stocks:us_technology_stocks` |
| As a result, Swiss exports is likely to ___ | ` increase` / ` decrease` | + | `swiss:swiss_exports` |
| As a result, Swiss pharmaceutical exports is likely to ___ | ` increase` / ` decrease` | + | `swiss:swiss_pharmaceutical_exports` |
| As a result, Switzerland's economic growth is likely to ___ | ` rise` / ` fall` | + | `swiss:switzerland_s_economic_growth` |
| As a result, the Swiss franc is likely to ___ | ` strengthen` / ` weaken` | − | `swiss:the_swiss_franc` |
| As a result, the risk of a conflict between China and Taiwan is likely to ___ | ` rise` / ` fall` | − | `taiwan:the_risk_of_a_conflict_between_china_and` |
| As a result, big tech earnings is likely to ___ | ` rise` / ` fall` | + | `tech:big_tech_earnings` |
| As a result, capital spending on artificial intelligence is likely to ___ | ` increase` / ` decrease` | + | `tech:capital_spending_on_artificial_intellige` |
| As a result, demand for AI chips is likely to ___ | ` increase` / ` decrease` | + | `tech:demand_for_ai_chips` |
| As a result, semiconductor demand is likely to ___ | ` increase` / ` decrease` | + | `tech:semiconductor_demand` |
| As a result, 10-year US Treasury yields is likely to ___ | ` rise` / ` fall` | − | `treasury:10_year_us_treasury_yields` |
| As a result, 2-year US Treasury yields is likely to ___ | ` rise` / ` fall` | − | `treasury:2_year_us_treasury_yields` |
| As a result, 30-year US Treasury yields is likely to ___ | ` rise` / ` fall` | − | `treasury:30_year_us_treasury_yields` |
| As a result, the US Treasury term premium is likely to ___ | ` rise` / ` fall` | − | `treasury:the_us_treasury_term_premium` |
| As a result, US bond market volatility is likely to ___ | ` rise` / ` fall` | − | `treasury:us_bond_market_volatility` |
| As a result, US real yields is likely to ___ | ` rise` / ` fall` | − | `treasury:us_real_yields` |
| As a result, US Treasury yields is likely to ___ | ` rise` / ` fall` | − | `treasury:us_treasury_yields` |
| As a result, sterling against the US dollar is likely to ___ | ` rise` / ` fall` | + | `uk:sterling_against_the_us_dollar` |
| As a result, the pound is likely to ___ | ` strengthen` / ` weaken` | + | `uk:the_pound` |
| As a result, the UK unemployment rate is likely to ___ | ` rise` / ` fall` | − | `uk:the_uk_unemployment_rate` |
| As a result, UK economic growth is likely to ___ | ` rise` / ` fall` | + | `uk:uk_economic_growth` |
| As a result, UK-EU trade relations is likely to ___ | ` improve` / ` worsen` | + | `uk:uk_eu_trade_relations` |
| As a result, UK public finances is likely to ___ | ` improve` / ` worsen` | + | `uk:uk_public_finances` |
| As a result, UK retail sales is likely to ___ | ` rise` / ` fall` | + | `uk:uk_retail_sales` |
| As a result, UK services activity is likely to ___ | ` expand` / ` contract` | + | `uk:uk_services_activity` |
| As a result, consumer confidence is likely to ___ | ` rise` / ` fall` | + | `usa:consumer_confidence` |
| As a result, the risk of a US recession is likely to ___ | ` rise` / ` fall` | − | `usa:the_risk_of_a_us_recession` |
| As a result, US business investment is likely to ___ | ` increase` / ` decrease` | + | `usa:us_business_investment` |
| As a result, US economic growth is likely to ___ | ` rise` / ` fall` | + | `usa:us_economic_growth` |
| As a result, US manufacturing activity is likely to ___ | ` expand` / ` contract` | + | `usa:us_manufacturing_activity` |
| As a result, US oil demand is likely to ___ | ` increase` / ` decrease` | + | `usa:us_oil_demand` |
| As a result, US retail sales is likely to ___ | ` rise` / ` fall` | + | `usa:us_retail_sales` |
| As a result, US services activity is likely to ___ | ` expand` / ` contract` | + | `usa:us_services_activity` |
| Relative to market expectations, the US CPI inflation print came in ___ | ` higher` / ` lower` | − | `usdata:the_us_cpi_inflation_print` |
| As a result, the risk of a US government shutdown is likely to ___ | ` rise` / ` fall` | − | `usfiscal:the_risk_of_a_us_government_shutdown` |
| As a result, the US labour market is likely to ___ | ` improve` / ` worsen` | + | `usjobs:the_us_labour_market` |
| As a result, US layoffs is likely to ___ | ` increase` / ` decrease` | − | `usjobs:us_layoffs` |
| As a result, US export controls on semiconductors is likely to ___ | ` tighten` / ` ease` | − | `uspolicy:us_export_controls_on_semiconductors` |
| As a result, US tariffs on imports is likely to ___ | ` tighten` / ` ease` | − | `uspolicy:us_tariffs_on_imports` |
| As a result, global economic growth is likely to ___ | ` rise` / ` fall` | + | `world:global_economic_growth` |
| As a result, global oil demand is likely to ___ | ` increase` / ` decrease` | + | `world:global_oil_demand` |
| As a result, the risk of a global recession is likely to ___ | ` rise` / ` fall` | − | `world:the_risk_of_a_global_recession` |
