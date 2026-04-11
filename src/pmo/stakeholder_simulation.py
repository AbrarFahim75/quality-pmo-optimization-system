def generate_stakeholder_view(role, summary, recommendations):
    if role == "Manager":
        return {
            "Focus": "Operational Performance",
            "Key Info": [
                f"Best Ship: {summary['best_ship']}",
                f"Worst Ship: {summary['worst_ship']}",
                f"Delayed Route: {summary['worst_route']}"
            ],
            "Action": recommendations
        }

    elif role == "Executive":
        return {
            "Focus": "Business Impact",
            "Key Info": [
                f"Profit Leader: {summary['best_ship']}",
                f"Risk Area: {summary['worst_route']}"
            ],
            "Action": ["Invest in high-performing ship types"]
        }

    elif role == "Engineer":
        return {
            "Focus": "Technical Efficiency",
            "Key Info": [
                f"Best Engine: {summary['best_engine']}"
            ],
            "Action": ["Optimize fuel efficiency", "Monitor engine performance"]
        }

    else:
        return {"Info": "No role selected"}