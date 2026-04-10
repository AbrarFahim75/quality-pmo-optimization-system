import pandas as pd

def load_data(path):
    df = pd.read_csv(path, parse_dates=["planned_date", "actual_date"])
    return df

if __name__ == "__main__":
    df = load_data("../../data/raw/shipping_data.csv")
    print(df.head())
