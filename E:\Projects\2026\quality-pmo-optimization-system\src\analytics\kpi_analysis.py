def compute_kpis(df):
    df = df.copy()

    df["Profit"] = df["Revenue_per_Voyage_USD"] - df["Operational_Cost_USD"]

    df["Efficiency_Level"] = df["Efficiency_nm_per_kWh"].apply(
        lambda x: "High" if x > 1.5 else ("Medium" if x > 1.0 else "Low")
    )

    df["Delay_Risk"] = df["Turnaround_Time_hours"].apply(
        lambda x: "High" if x > 50 else "Low"
    )

    return df
