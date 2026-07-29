import requests
import pandas as pd

scheme_codes = {
    "HDFC Top 100": 125497,
    "SBI Bluechip": 119551,
    "ICICI Bluechip": 120503,
    "Nippon Large Cap": 118632,
    "Axis Bluechip": 119092,
    "Kotak Bluechip": 120841
}

for name, code in scheme_codes.items():
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        df = pd.DataFrame(data["data"])

        filename = f"data/raw/{name.replace(' ', '_')}_nav.csv"

        df.to_csv(filename, index=False)

        print(f"{name} downloaded successfully.")
    else:
        print(f"Failed to fetch {name}")