# Data Dictionary

## 01_fund_master.csv

| Column        | Type    | Description             |
| ------------- | ------- | ----------------------- |
| amfi_code     | Integer | Unique AMFI scheme code |
| fund_house    | Text    | Mutual fund company     |
| scheme_name   | Text    | Name of scheme          |
| category      | Text    | Scheme category         |
| sub_category  | Text    | Scheme sub-category     |
| risk_category | Text    | Risk level              |

## 02_nav_history.csv

| Column    | Type    | Description     |
| --------- | ------- | --------------- |
| amfi_code | Integer | Scheme code     |
| date      | Date    | NAV date        |
| nav       | Decimal | Net Asset Value |

## 08_investor_transactions.csv

| Column           | Type    | Description             |
| ---------------- | ------- | ----------------------- |
| investor_id      | Text    | Investor identifier     |
| transaction_date | Date    | Transaction date        |
| transaction_type | Text    | SIP/Lumpsum/Redemption  |
| amount_inr       | Decimal | Transaction amount      |
| kyc_status       | Text    | KYC verification status |

## 07_scheme_performance.csv

| Column            | Type    | Description             |
| ----------------- | ------- | ----------------------- |
| return_1yr_pct    | Decimal | 1 year return           |
| return_3yr_pct    | Decimal | 3 year return           |
| return_5yr_pct    | Decimal | 5 year return           |
| expense_ratio_pct | Decimal | Expense ratio           |
| aum_crore         | Decimal | Assets under management |
