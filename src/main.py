import pandas as pd
from src.analysis.kpi_analysis import compute_kpis

def main():
    df = pd.read_csv("data/raw/ship_performance.csv")

    df = compute_kpis(df)

    print("KPI Analysis Done\n")
    print(df[["Profit", "Efficiency_Level", "Delay_Risk"]].head())

if __name__ == "__main__":
    main()
