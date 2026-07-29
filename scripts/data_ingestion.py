import pandas as pd 
import os

data_path = "data/raw"

for file in os.listdir(data_path):
    if file.endswith(".csv"):
        file_path = os.path.join(data_path,file)
        df = pd.read_csv(file_path)
        print("=" * 60 )
        print("File:",file)
        print("Shape:",df.shape)
        print("\nData Types:")
        print(df.dtypes)
        print("\nFirst 5 Rows:")
        print(df.head())
