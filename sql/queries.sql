SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM "07_scheme_performance"
ORDER BY aum_crore DESC
LIMIT 5;


SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav),2) AS avg_nav
FROM "02_nav_history"
GROUP BY month
ORDER BY month;


SELECT
    month,
    yoy_growth_pct
FROM "04_monthly_sip_inflows"
ORDER BY month;


SELECT
    state,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr),2) AS total_amount
FROM "08_investor_transactions"
GROUP BY state
ORDER BY total_amount DESC;


SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM "07_scheme_performance"
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


SELECT
    scheme_name,
    return_3yr_pct
FROM "07_scheme_performance"
ORDER BY return_3yr_pct DESC
LIMIT 10;


SELECT
    category,
    ROUND(AVG(expense_ratio_pct),2) AS avg_expense_ratio
FROM "07_scheme_performance"
GROUP BY category
ORDER BY avg_expense_ratio;

SELECT
    stock_name,
    sector,
    weight_pct
FROM "09_portfolio_holdings"
ORDER BY weight_pct DESC
LIMIT 10;


SELECT
    payment_mode,
    ROUND(AVG(amount_inr),2) AS avg_amount
FROM "08_investor_transactions"
GROUP BY payment_mode
ORDER BY avg_amount DESC;


SELECT
    index_name,
    date,
    close_value
FROM "10_benchmark_indices"
ORDER BY date DESC;