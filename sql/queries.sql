-- 1. Top 5 Funds by AUM
SELECT * FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV
SELECT AVG(nav) FROM fact_nav;

-- 3. Average NAV by AMFI Code
SELECT amfi_code, AVG(nav)
FROM fact_nav
GROUP BY amfi_code;

-- 4. Total Transactions by State
SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state;

-- 5. Funds with Expense Ratio < 1%
SELECT amfi_code, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Total Investment Amount
SELECT SUM(amount_inr)
FROM fact_transactions;

-- 7. Transaction Type Distribution
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 8. Highest 1-Year Return
SELECT amfi_code, return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- 9. Average Expense Ratio
SELECT AVG(expense_ratio_pct)
FROM fact_performance;

-- 10. Count Funds by Category
SELECT category, COUNT(*)
FROM fact_performance
GROUP BY category;
