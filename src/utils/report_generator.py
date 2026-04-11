def generate_report(summary, recommendations):
    report = f"""
==============================
     PROJECT REPORT
==============================

📊 PERFORMANCE SUMMARY

Best Ship Type       : {summary['best_ship']}
Worst Ship Type      : {summary['worst_ship']}
Most Delayed Route   : {summary['worst_route']}
Best Engine Type     : {summary['best_engine']}

===================================
       🚀 RECOMMENDATIONS
===================================
"""

    for rec in recommendations:
        report += f"- {rec}\n"

    return report


def save_report(report):
    with open("reports/generated_report.md", "w") as f:
        f.write(report)