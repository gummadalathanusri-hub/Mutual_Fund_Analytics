import pandas as pd
import os

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]


for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")


df["anomaly"] = df[return_columns].isnull().any(axis=1)


df["expense_ratio_pct"] = pd.to_numeric(df["expense_ratio_pct"], errors="coerce")

df = df[
    (df["expense_ratio_pct"] >= 0.1) &
    (df["expense_ratio_pct"] <= 2.5)
]


df = df.drop_duplicates()


os.makedirs("data/processed", exist_ok=True)


df.to_csv(
    "data/processed/07_scheme_performance.csv",
    index=False
)

print("Scheme Performance cleaned successfully!")
print("Final Shape:", df.shape)
print("Anomalies:", df["anomaly"].sum())