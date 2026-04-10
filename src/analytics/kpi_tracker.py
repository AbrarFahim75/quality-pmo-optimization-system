def calculate_kpis(df):
    total_projects = len(df)
    
    on_time = df[df["delay_days"] <= 0].shape[0]
    delayed = df[df["delay_days"] > 0].shape[0]

    on_time_rate = on_time / total_projects * 100
    avg_delay = df["delay_days"].mean()

    return {
        "total_projects": total_projects,
        "on_time_rate": round(on_time_rate, 2),
        "average_delay": round(avg_delay, 2),
        "delayed_projects": delayed
    }
