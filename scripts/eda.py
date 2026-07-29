import pandas as pd
import os

processed_path = "data/processed"

for file in os.listdir(processed_path):

    if file.endswith(".csv"):

        file_path = os.path.join(processed_path, file)

        df = pd.read_csv(file_path)

        print("\n" + "="*60)
        print("File:", file)
        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("\nNumber of Rows and Columns:")
        print(df.shape)
        
        print("\nColumn Names:")
        print(df.columns.tolist())
        
        print("\nMemory Usage:")
        print(df.memory_usage(deep=True))
        
        print("\nMissing Value Percentage:")
        print((df.isnull().sum() / len(df)) * 100)

        print("\nData Types:")
        print(df.dtypes)

        print("\nNumerical Summary:")
        print(df.describe())

        print("\nCategorical Summary:")
        print(df.describe(include='all'))