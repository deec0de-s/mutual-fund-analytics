# ============================================================
# D6 - SIMPLE FUND RECOMMENDER
# ============================================================

import pandas as pd
from pathlib import Path


# ============================================================
# 1. PROJECT PATH
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
REPORTS_DIR = PROJECT_ROOT / "reports"


# ============================================================
# 2. FILE PATHS
# ============================================================

fund_master_path = PROCESSED_DIR / "01_fund_master.csv"
sharpe_path = REPORTS_DIR / "sharpe_ratio.csv"


# ============================================================
# 3. LOAD DATA
# ============================================================

try:
    fund_master_df = pd.read_csv(fund_master_path)
    sharpe_df = pd.read_csv(sharpe_path)

except FileNotFoundError as e:
    print("❌ File not found.")
    print(f"Details: {e}")
    raise SystemExit(1)


print("✅ Fund master loaded")
print(f"Shape: {fund_master_df.shape}")

print("\nFund master columns:")
print(fund_master_df.columns.tolist())

print("\nSharpe ratio columns:")
print(sharpe_df.columns.tolist())


# ============================================================
# 4. MERGE FUND INFORMATION + SHARPE RATIO
# ============================================================

recommender_df = fund_master_df.merge(
    sharpe_df,
    on="amfi_code",
    how="inner"
)


print("\n✅ Fund data and Sharpe ratios merged")
print(f"Total funds available: {len(recommender_df)}")


# ============================================================
# 5. RISK APPETITE MAPPING
# ============================================================

risk_mapping = {
    "Low": "Low",
    "Moderate": "Moderate",
    "High": "Very High"
}


# ============================================================
# 6. RECOMMENDER FUNCTION
# ============================================================

def recommend_funds(risk_appetite):
    """
    Recommend the top 3 mutual funds based on
    Sharpe Ratio for the selected risk appetite.

    Risk appetite options:
        Low
        Moderate
        High
    """

    if risk_appetite not in risk_mapping:
        raise ValueError(
            "Risk appetite must be: Low, Moderate, or High"
        )

    risk_category = risk_mapping[risk_appetite]

    recommendations = (
        recommender_df[
            recommender_df["risk_category"] == risk_category
        ]
        .sort_values(
            "Sharpe_Ratio",
            ascending=False
        )
        .head(3)
        [[
            "amfi_code",
            "scheme_name",
            "category",
            "plan",
            "risk_category",
            "Sharpe_Ratio"
        ]]
        .reset_index(drop=True)
    )

    return recommendations


# ============================================================
# 7. TEST ALL RISK APPETITES
# ============================================================

for appetite in ["Low", "Moderate", "High"]:

    print("\n" + "=" * 60)
    print(f"Recommendations for {appetite} Risk Appetite")
    print("=" * 60)

    result = recommend_funds(appetite)

    if result.empty:
        print("⚠️ No matching funds found.")

    else:
        print(
            result.to_string(index=False)
        )


# ============================================================
# 8. FINAL STATUS
# ============================================================

print("\n" + "=" * 60)
print("✅ FUND RECOMMENDER COMPLETED SUCCESSFULLY")
print("=" * 60)