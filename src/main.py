import pandas as pd
from src.analytics.kpi_tracker import compute_kpis
from src.analytics.insights import get_insights, generate_summary
from src.process.optimizer import generate_recommendations


def main():
    # Load data
    df = pd.read_csv("data/raw/ship_performance.csv")

    # KPI calculation
    df = compute_kpis(df)

    # Generate insights
    insights = get_insights(df)
    summary = generate_summary(insights)

    print("\n==============================")
    print("   KPI & INSIGHTS REPORT")
    print("==============================\n")

    # Detailed insights
    print("📊 Profit by Ship Type:")
    print(insights["profit_by_ship"], "\n")

    print("⏱️ Delay by Route Type:")
    print(insights["delay_by_route"], "\n")

    print("⚙️ Efficiency by Engine Type:")
    print(insights["efficiency_by_engine"], "\n")

    # Summary insights
    print("===================================")
    print("       🔥 SUMMARY INSIGHTS")
    print("===================================\n")

    print(f"✅ Best Ship Type       : {summary['best_ship']}")
    print(f"❌ Worst Ship Type      : {summary['worst_ship']}")
    print(f"⚠️ Most Delayed Route  : {summary['worst_route']}")
    print(f"🚀 Best Engine Type    : {summary['best_engine']}\n")
    
        # 🔥 Optimization Recommendations
    recommendations = generate_recommendations(summary)

    print("===================================")
    print("     🚀 RECOMMENDATIONS")
    print("===================================\n")

    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. {rec}")


if __name__ == "__main__":
    main()