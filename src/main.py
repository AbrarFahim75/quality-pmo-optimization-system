from src.data.load_data import load_data
from src.analytics.kpi_tracker import calculate_kpis
from src.analytics.delay_analysis import analyze_delays
from src.analytics.root_cause import root_cause_analysis
from src.pmo.project_tracker import track_projects
from src.process.optimization import optimization_recommendations


def main():
    print("🚀 Starting PMO Quality System...\n")

    df = load_data("data/raw/shipping_data.csv")

    # KPI
    kpis = calculate_kpis(df)
    print("📊 KPI Summary:")
    for key, value in kpis.items():
        print(f"{key}: {value}")

    # Delay Analysis
    delays = analyze_delays(df)
    print("\n⏱ Delay Analysis:")
    print(delays)

    # Root Cause
    print("\n🔍 Root Cause (by Stakeholder):")
    print(root_cause_analysis(df))

    # Project Tracking
    print("\n📁 Project Overview:")
    print(track_projects(df))

    # Optimization
    print("\n⚙️ Optimization Insight:")
    print(optimization_recommendations(df))


if __name__ == "__main__":
    main()
