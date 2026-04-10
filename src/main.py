from data.load_data import load_data
from analytics.kpi_tracker import calculate_kpis

def main():
    df = load_data("../data/raw/shipping_data.csv")
    kpis = calculate_kpis(df)

    print("📊 KPI Summary:")
    for key, value in kpis.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
