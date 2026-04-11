def generate_recommendations(summary):

    recommendations = []

    # Ship performance
    if summary["worst_ship"]:
        recommendations.append(
            f"Improve performance of {summary['worst_ship']} ships (low profitability)."
        )

    # Route delay
    if summary["worst_route"]:
        recommendations.append(
            f"Optimize operations on {summary['worst_route']} routes to reduce delays."
        )

    # Engine efficiency
    if summary["best_engine"]:
        recommendations.append(
            f"Consider adopting {summary['best_engine']} engines for better efficiency."
        )

    return recommendations