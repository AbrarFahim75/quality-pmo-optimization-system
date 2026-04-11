import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import plotly.express as px

# Analytics
from src.analytics.kpi_tracker import compute_kpis
from src.analytics.insights import get_insights, generate_summary
from src.process.optimizer import generate_recommendations

# PMO + Process + Reporting
from src.pmo.project_tracker import create_project_status
from src.pmo.stakeholder_simulation import generate_stakeholder_view
from src.process.current_state import current_process
from src.process.future_state import future_process
from src.utils.report_generator import generate_report


# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(layout="wide")


# ==============================
# SIDEBAR
# ==============================
st.sidebar.title("Navigation")

section = st.sidebar.radio(
    "Go to",
    ["Dashboard", "PMO View", "Process View", "Stakeholder View"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Project Info")
st.sidebar.write("Maritime Optimization System")
st.sidebar.write("Author: Md Abrar Fahim")

# ==============================
# TITLE
# ==============================
st.title("Maritime Performance Optimization System")
st.markdown("### Analytics & Decision Support Dashboard")
st.markdown("---")


# ==============================
# LOAD DATA
# ==============================
df = pd.read_csv("data/raw/ship_performance.csv")
df = compute_kpis(df)


# ==============================
# FILTERS
# ==============================
st.sidebar.markdown("### Filters")

ship_type = st.sidebar.selectbox(
    "Ship Type", ["All"] + list(df["Ship_Type"].unique())
)

route_type = st.sidebar.selectbox(
    "Route Type", ["All"] + list(df["Route_Type"].unique())
)

engine_type = st.sidebar.selectbox(
    "Engine Type", ["All"] + list(df["Engine_Type"].unique())
)

filtered_df = df.copy()

if ship_type != "All":
    filtered_df = filtered_df[filtered_df["Ship_Type"] == ship_type]

if route_type != "All":
    filtered_df = filtered_df[filtered_df["Route_Type"] == route_type]

if engine_type != "All":
    filtered_df = filtered_df[filtered_df["Engine_Type"] == engine_type]

st.sidebar.write(f"Filtered rows: {filtered_df.shape[0]}")


# ==============================
# INSIGHTS
# ==============================
insights = get_insights(filtered_df)
summary = generate_summary(insights)
recommendations = generate_recommendations(summary)


# ==============================
# DASHBOARD
# ==============================
if section == "Dashboard":

    # ==============================
    # KPI SECTION
    # ==============================
    st.markdown("## Key Performance Indicators")
    st.caption("Aggregated performance metrics based on selected filters")

    col1, col2, col3 = st.columns(3)

    col1.metric("Average Profit", f"${filtered_df['Profit'].mean():,.0f}")
    col2.metric("Average Delay (hrs)", f"{filtered_df['Turnaround_Time_hours'].mean():.2f}")
    col3.metric("Efficiency (nm/kWh)", f"{filtered_df['Efficiency_nm_per_kWh'].mean():.2f}")

    st.markdown("---")

    # ==============================
    # DATA OVERVIEW
    # ==============================
    st.markdown("## Operational Data Snapshot")

    st.write(f"Rows: {filtered_df.shape[0]} | Columns: {filtered_df.shape[1]}")

    st.write("### Preview (First 5 rows)")
    st.dataframe(filtered_df.head(), use_container_width=True)

    with st.expander("View Full Dataset"):
        st.dataframe(filtered_df, height=500, use_container_width=True)

    st.markdown("---")

    # ==============================
    # PERFORMANCE ANALYSIS
    # ==============================
    st.markdown("## Performance Analysis")

    col1, col2 = st.columns(2)

    # -------- PROFIT (Highlight Best/Worst) --------
    df_profit = insights["profit_by_ship"].reset_index()

    df_profit["Highlight"] = df_profit["Ship_Type"].apply(
        lambda x: "Best" if x == summary["best_ship"]
        else "Worst" if x == summary["worst_ship"]
        else "Normal"
    )

    fig1 = px.bar(
        df_profit,
        x="Ship_Type",
        y="Profit",
        color="Highlight",
        color_discrete_map={
            "Best": "green",
            "Worst": "red",
            "Normal": "lightgray"
        },
        title="Profit by Ship Type"
    )

    fig1.update_traces(marker_line_color='black', marker_line_width=1, opacity=0.9)
    fig1.update_layout(plot_bgcolor="white", paper_bgcolor="white", font=dict(size=14))

    with col1:
        st.plotly_chart(fig1, use_container_width=True)

    # -------- DELAY --------
    fig2 = px.bar(
        insights["delay_by_route"].reset_index(),
        x="Route_Type",
        y="Turnaround_Time_hours",
        title="Delay by Route Type",
        color="Turnaround_Time_hours",
        color_continuous_scale="Reds_r"
    )

    fig2.update_traces(marker_line_color='black', marker_line_width=1, opacity=0.9)
    fig2.update_layout(plot_bgcolor="white", paper_bgcolor="white", font=dict(size=14))

    with col2:
        st.plotly_chart(fig2, use_container_width=True)

    # -------- EFFICIENCY --------
    fig3 = px.bar(
        insights["efficiency_by_engine"].reset_index(),
        x="Engine_Type",
        y="Efficiency_nm_per_kWh",
        title="Efficiency by Engine Type",
        color="Efficiency_nm_per_kWh",
        color_continuous_scale="Greens_r"
    )

    fig3.update_traces(marker_line_color='black', marker_line_width=1, opacity=0.9)
    fig3.update_layout(plot_bgcolor="white", paper_bgcolor="white", font=dict(size=14))

    st.plotly_chart(fig3, use_container_width=True)

    # ==============================
    # KEY OBSERVATIONS (CARD STYLE)
    # ==============================
    st.markdown("### Key Observations")

    st.info(f"""
    • Most profitable ship type: **{summary['best_ship']}**  
    • Lowest performing ship type: **{summary['worst_ship']}**  
    • Highest delays observed on: **{summary['worst_route']}**  
    • Most efficient engine type: **{summary['best_engine']}**
    """)

    st.markdown("---")

    # ==============================
    # SUMMARY
    # ==============================
    st.markdown("## Summary Insights")

    st.write(f"Best Ship Type: {summary['best_ship']}")
    st.write(f"Worst Ship Type: {summary['worst_ship']}")
    st.write(f"Most Delayed Route: {summary['worst_route']}")
    st.write(f"Best Engine Type: {summary['best_engine']}")

    st.markdown("---")

    # ==============================
    # RECOMMENDATIONS
    # ==============================
    st.markdown("## Recommendations")

    for rec in recommendations:
        st.write(f"- {rec}")

    st.markdown("---")

    # ==============================
    # REPORT
    # ==============================
    st.markdown("## Project Report")

    report = generate_report(summary, recommendations)

    st.text(report)

    st.download_button(
        label="Download Report",
        data=report,
        file_name="project_report.txt",
        mime="text/plain"
    )


# ==============================
# PMO VIEW
# ==============================
elif section == "PMO View":

    st.markdown("## Project Status")

    project = create_project_status()
    st.json(project)


# ==============================
# PROCESS VIEW
# ==============================
elif section == "Process View":

    st.markdown("## Process Comparison")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Current State")
        st.json(current_process())

    with col2:
        st.subheader("Future State")
        st.json(future_process())


# ==============================
# STAKEHOLDER VIEW
# ==============================
elif section == "Stakeholder View":

    st.markdown("## Stakeholder Perspective")

    role = st.selectbox(
        "Select Stakeholder Role",
        ["Manager", "Executive", "Engineer"]
    )

    view = generate_stakeholder_view(role, summary, recommendations)

    st.subheader(f"{role} View")

    st.write("Focus Area:", view["Focus"])

    st.write("Key Insights:")
    for item in view["Key Info"]:
        st.write(f"- {item}")

    st.write("Recommended Actions:")
    for action in view["Action"]:
        st.write(f"- {action}")


# ==============================
# FOOTER
# ==============================
st.markdown("---")
st.caption("Maritime Performance Optimization System | Data Analytics & PMO Dashboard")