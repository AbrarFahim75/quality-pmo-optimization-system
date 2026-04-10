def root_cause_analysis(df):
    return df.groupby("stakeholder")["delay_days"].mean().sort_values(ascending=False)
