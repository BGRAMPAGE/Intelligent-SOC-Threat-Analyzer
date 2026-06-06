import pandas as pd


def load_data(file_path):

    try:

        print("Loading dataset...")

        df = pd.read_csv(file_path)

        print("Dataset Loaded Successfully")

        print(f"Rows    : {len(df)}")
        print(f"Columns : {len(df.columns)}")

        return df

    except Exception as e:

        print(f"Error Loading Dataset: {e}")

        return None