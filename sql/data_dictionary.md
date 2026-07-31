# Mutual Fund Analytics - Data Dictionary

## 01_fund_master

| Column | Data Type | Business Definition | Source |
|---------|-----------|---------------------|--------|
| amfi_code | INTEGER | Unique AMFI scheme code | AMFI |
| fund_house | TEXT | Mutual fund company | AMFI |
| scheme_name | TEXT | Name of the scheme | AMFI |
| category | TEXT | Fund category | AMFI |
| sub_category | TEXT | Fund sub-category | AMFI |
| plan | TEXT | Regular/Direct plan | AMFI |
| launch_date | DATE | Scheme launch date | AMFI |
| benchmark | TEXT | Benchmark index | AMFI |
| expense_ratio_pct | REAL | Expense ratio (%) | AMFI |
| exit_load_pct | REAL | Exit load (%) | AMFI |
| min_sip_amount | REAL | Minimum SIP amount | AMFI |
| min_lumpsum_amount | REAL | Minimum lump sum amount | AMFI |
| fund_manager | TEXT | Fund manager name | AMFI |
| risk_category | TEXT | Risk level | AMFI |
| sebi_category_code | TEXT | SEBI category code | SEBI |

---

## 02_nav_history

| Column | Data Type | Business Definition | Source |
|---------|-----------|---------------------|--------|
| amfi_code | INTEGER | Scheme code | AMFI |
| date | DATE | NAV date | AMFI |
| nav | REAL | Net Asset Value | AMFI |

---

## 03_aum_by_fund_house

| Column | Data Type | Business Definition | Source |
|---------|-----------|---------------------|--------|
| date | DATE | Report date | AMFI |
| fund_house | TEXT | Fund house | AMFI |
| aum_lakh_crore | REAL | AUM (Lakh Crore) | AMFI |
| aum_crore | REAL | Assets Under Management | AMFI |
| num_schemes | INTEGER | Number of schemes | AMFI |

---

## 04_monthly_sip_inflows

| Column | Data Type | Business Definition | Source |
|---------|-----------|---------------------|--------|
| month | TEXT | Reporting month | AMFI |
| sip_inflow_crore | REAL | SIP inflow | AMFI |
| active_sip_accounts_crore | REAL | Active SIP accounts | AMFI |
| new_sip_accounts_lakh | REAL | New SIP accounts | AMFI |
| sip_aum_lakh_crore | REAL | SIP AUM | AMFI |
| yoy_growth_pct | REAL | Year-over-Year growth | AMFI |

---

## 05_category_inflows

| Column | Data Type | Business Definition | Source |
|---------|-----------|---------------------|--------|
| month | TEXT | Reporting month | AMFI |
| category | TEXT | Fund category | AMFI |
| net_inflow_crore | REAL | Net inflow | AMFI |

---

## 06_industry_folio_count

| Column | Data Type | Business Definition | Source |
|---------|-----------|---------------------|--------|
| month | TEXT | Reporting month | AMFI |
| total_folios_crore | REAL | Total folios | AMFI |
| equity_folios_crore | REAL | Equity folios | AMFI |
| debt_folios_crore | REAL | Debt folios | AMFI |
| hybrid_folios_crore | REAL | Hybrid folios | AMFI |
| others_folios_crore | REAL | Other folios | AMFI |

---

## 07_scheme_performance

| Column | Data Type | Business Definition | Source |
|---------|-----------|---------------------|--------|
| amfi_code | INTEGER | Scheme code | AMFI |
| scheme_name | TEXT | Scheme name | AMFI |
| fund_house | TEXT | Fund house | AMFI |
| category | TEXT | Category | AMFI |
| plan | TEXT | Plan type | AMFI |
| return_1yr_pct | REAL | 1-Year Return | AMFI |
| return_3yr_pct | REAL | 3-Year Return | AMFI |
| return_5yr_pct | REAL | 5-Year Return | AMFI |
| benchmark_3yr_pct | REAL | Benchmark Return | AMFI |
| alpha | REAL | Alpha | AMFI |
| beta | REAL | Beta | AMFI |
| sharpe_ratio | REAL | Sharpe Ratio | AMFI |
| sortino_ratio | REAL | Sortino Ratio | AMFI |
| std_dev_ann_pct | REAL | Annual Std. Deviation | AMFI |
| max_drawdown_pct | REAL | Maximum Drawdown | AMFI |
| aum_crore | REAL | AUM | AMFI |
| expense_ratio_pct | REAL | Expense Ratio | AMFI |
| morningstar_rating | INTEGER | Morningstar Rating | Morningstar |
| risk_grade | TEXT | Risk Grade | AMFI |
| anomaly | BOOLEAN | Validation Flag | Generated |

---

## 08_investor_transactions

| Column | Data Type | Business Definition | Source |
|---------|-----------|---------------------|--------|
| investor_id | INTEGER | Investor ID | Internal |
| transaction_date | DATE | Transaction Date | Internal |
| amfi_code | INTEGER | Scheme Code | AMFI |
| transaction_type | TEXT | SIP/Lumpsum/Redemption | Internal |
| amount_inr | REAL | Transaction Amount | Internal |
| state | TEXT | Investor State | Internal |
| city | TEXT | Investor City | Internal |
| city_tier | TEXT | City Tier | Internal |
| age_group | TEXT | Investor Age Group | Internal |
| gender | TEXT | Gender | Internal |
| annual_income_lakh | REAL | Annual Income | Internal |
| payment_mode | TEXT | Payment Mode | Internal |
| kyc_status | TEXT | KYC Status | Internal |

---

## 09_portfolio_holdings

| Column | Data Type | Business Definition | Source |
|---------|-----------|---------------------|--------|
| amfi_code | INTEGER | Scheme Code | AMFI |
| stock_symbol | TEXT | Stock Symbol | NSE/BSE |
| stock_name | TEXT | Stock Name | NSE/BSE |
| sector | TEXT | Sector | NSE/BSE |
| weight_pct | REAL | Portfolio Weight | AMFI |
| market_value_cr | REAL | Market Value | AMFI |
| current_price_inr | REAL | Current Price | NSE/BSE |
| portfolio_date | DATE | Portfolio Date | AMFI |

---

## 10_benchmark_indices

| Column | Data Type | Business Definition | Source |
|---------|-----------|---------------------|--------|
| date | DATE | Trading Date | NSE |
| index_name | TEXT | Benchmark Index | NSE |
| close_value | REAL | Closing Value | NSE |