CREATE TABLE dim_fund (
amfi_code INTEGER PRIMARY KEY,
scheme_name TEXT,
fund_house TEXT,
category TEXT
);

CREATE TABLE dim_date (
date_id INTEGER PRIMARY KEY,
full_date DATE
);

CREATE TABLE fact_nav (
amfi_code INTEGER,
date DATE,
nav REAL
);

CREATE TABLE fact_transactions (
investor_id TEXT,
transaction_date DATE,
amfi_code INTEGER,
transaction_type TEXT,
amount_inr REAL
);

CREATE TABLE fact_performance (
amfi_code INTEGER,
return_1yr_pct REAL,
return_3yr_pct REAL,
return_5yr_pct REAL,
expense_ratio_pct REAL
);

CREATE TABLE fact_aum (
amfi_code INTEGER,
aum_crore REAL
);
