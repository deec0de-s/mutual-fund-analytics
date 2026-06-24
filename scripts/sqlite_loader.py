import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned datasets

nav = pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
)

txn = pd.read_csv(
    "data/processed/08_investor_transactions_cleaned.csv"
)

perf = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

txn.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("SQLite Database Created Successfully")