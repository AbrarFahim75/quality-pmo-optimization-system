def get_insights(df):

    insights = {}

    # 1. Average profit by ship type
    insights["profit_by_ship"] = df.groupby("Ship_Type")["Profit"].mean()

    # 2. Average delay risk by route
    insights["delay_by_route"] = df.groupby("Route_Type")["Turnaround_Time_hours"].mean()

    # 3. Efficiency by engine type
    insights["efficiency_by_engine"] = df.groupby("Engine_Type")["Efficiency_nm_per_kWh"].mean()

    return insights

def generate_summary(insights):
    summary = {}

    # Best ship type
    summary["best_ship"] = insights["profit_by_ship"].idxmax()

    # Worst ship type
    summary["worst_ship"] = insights["profit_by_ship"].idxmin()

    # Most delayed route
    summary["worst_route"] = insights["delay_by_route"].idxmax()

    # Best engine
    summary["best_engine"] = insights["efficiency_by_engine"].idxmax()

    return summary