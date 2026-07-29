import pandas as pd
df = pd.read_csv("data/processed/01_fund_master.csv")

print("=" * 60)
print("FUND MASTER ANALYSIS")
print("=" * 60)

print("\nTotal Records:")
print(len(df))

print("\nColumns:")
print(df.columns.tolist())

for col in df.columns:
    col_lower = col.lower()

    if "house" in col_lower:
        print(f"\nUnique {col}:")
        print(df[col].unique())

    elif "category" in col_lower:
        print(f"\nUnique {col}:")
        print(df[col].unique())

    elif "sub" in col_lower:
        print(f"\nUnique {col}:")
        print(df[col].unique())

    elif "risk" in col_lower:
        print(f"\nUnique {col}:")
        print(df[col].unique())