from src.analytics.kpi_tracker import calculate_kpis
import pandas as pd

def test_kpi():
    df = pd.DataFrame({"delay_days": [0, 1, 2]})
    result = calculate_kpis(df)
    assert "total_projects" in result
