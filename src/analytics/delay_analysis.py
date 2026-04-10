def analyze_delays(df):
    delayed_df = df[df["delay_days"] > 0]

    return {
        "total_delays": len(delayed_df),
        "avg_delay": delayed_df["delay_days"].mean(),
        "max_delay": delayed_df["delay_days"].max()
    }
