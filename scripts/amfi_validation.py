import pandas as pd

fund_master = pd.read_csv("data/processed/01_fund_master.csv")
nav_history = pd.read_csv("data/processed/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing = fund_codes - nav_codes

print("=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

print("Total Fund Master Codes:", len(fund_codes))
print("Total NAV History Codes:", len(nav_codes))

if len(missing) == 0:
    print("\nAll AMFI codes are present in nav_history.csv")
else:
    print("\nMissing AMFI Codes:")
    print(missing)