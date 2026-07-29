import pandas as pd
import os

raw_path = "data/raw"
processed_path = "data/processed"
os.makedirs(processed_path, exist_ok=True)

for file in os.listdir(raw_path):
    if file.endswith(".csv"):

        file_path = os.path.join(raw_path, file)
        df = pd.read_csv(file_path)
        df = df.drop_duplicates()
        df.columns = df.columns.str.strip()
        for col in df.select_dtypes(include=["object","string"]).columns:
            df[col] = df[col].astype(str).str.strip()
        output_path = os.path.join(processed_path, file)
        df.to_csv(output_path, index=False)
        print(f"{file} cleaned and saved successfully.")