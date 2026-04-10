def milestone_status(df):
    return df[["project_name", "planned_date", "actual_date", "delay_days"]]
