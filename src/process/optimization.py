def optimization_recommendations(df):
    if df["delay_days"].mean() > 1:
        return "High delays detected: Recommend process optimization."
    return "System operating efficiently."
