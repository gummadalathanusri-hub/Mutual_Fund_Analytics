import os
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

processed_path = "data/processed"

for file in os.listdir(processed_path):

    if file.endswith(".csv"):

        table_name = file.replace(".csv", "")

        file_path = os.path.join(processed_path, file)

        df = pd.read_csv(file_path)

        
        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(f"{table_name} loaded successfully.")
        print(f"Rows loaded: {len(df)}")

print("\nAll datasets loaded successfully!")