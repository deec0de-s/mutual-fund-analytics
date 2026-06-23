import pandas as pd

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    print("\n" + "=" * 50)
    print("Reading:", file)

    path = "data/raw/" + file

    df = pd.read_csv(path)

    print("Rows and Columns:")
    print(df.shape)

    print("\nColumn Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())