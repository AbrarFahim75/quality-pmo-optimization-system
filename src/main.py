import pandas as pd

def main():
    df = pd.read_csv("data/raw/ship_performance.csv")

    print("Dataset loaded successfully\n")
    print(df.head())

    print("\nColumns:\n")
    print(df.columns)

if __name__ == "__main__":
    main()