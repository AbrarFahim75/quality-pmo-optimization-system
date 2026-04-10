import pandas as pd

def preprocess_data(df):
    df = df.copy()
    
    # Handle missing values
    df = df.fillna(0)

    # Ensure delay is numeric
    df["delay_days"] = pd.to_numeric(df["delay_days"], errors="coerce")

    return df
