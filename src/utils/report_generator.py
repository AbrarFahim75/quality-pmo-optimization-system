def generate_report(summary, recommendations):
    report = f"""
PROJECT REPORT

Best Ship: {summary['best_ship']}
Worst Ship: {summary['worst_ship']}
Most Delayed Route: {summary['worst_route']}

RECOMMENDATIONS:
"""

    for rec in recommendations:
        report += f"- {rec}\n"

    return report