import sys
import os

# Fix import path for src modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd

# Analytics imports
from src.analytics.kpi_tracker import compute_kpis
from src.analytics.insights import get_insights, generate_summary
from src.process.optimizer import generate_recommendations

# PMO + Process + Reporting
from src.pmo.project_tracker import create_project_status
from src.process.current_state import current_process
from src.process.future_state import future_process
from src.utils.report_generator import generate_report


# ==============================
# TITLE
# ==============================
st.title("🚢 AI-Powered Maritime Performance Optimization System")


# ==============================
# LOAD DATA
# ==============================
df = pd.read_csv("data/raw/ship_performance.csv")
df = compute_kpis(df)


# ==============================
# FILTERS (INTERACTIVE)
# ==============================
st.sidebar.header("🔍 Filters")

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


# ==============================
# INSIGHTS + RECOMMENDATIONS
# ==============================
insights = get_insights(filtered_df)
summary = generate_summary(insights)
recommendations = generate_recommendations(summary)


# ==============================
# KPI METRICS
# ==============================
st.header("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Profit", round(filtered_df["Profit"].mean(), 2))
col2.metric("Avg Delay", round(filtered_df["Turnaround_Time_hours"].mean(), 2))
col3.metric("Avg Efficiency", round(filtered_df["Efficiency_nm_per_kWh"].mean(), 2))


# ==============================
# DATA OVERVIEW
# ==============================
st.header("📊 Raw Operational Data")
st.dataframe(filtered_df.head())


# ==============================
# ANALYTICS
# ==============================
st.header("📈 Analytics")

st.subheader("Profit by Ship Type")
st.bar_chart(insights["profit_by_ship"])

st.subheader("Delay by Route Type")
st.bar_chart(insights["delay_by_route"])

st.subheader("Efficiency by Engine Type")
st.bar_chart(insights["efficiency_by_engine"])


# ==============================
# SUMMARY
# ==============================
st.header("🔥 Summary Insights")

st.write(f"✅ Best Ship Type: {summary['best_ship']}")
st.write(f"❌ Worst Ship Type: {summary['worst_ship']}")
st.write(f"⚠️ Most Delayed Route: {summary['worst_route']}")
st.write(f"🚀 Best Engine Type: {summary['best_engine']}")


# ==============================
# RECOMMENDATIONS
# ==============================
st.header("🚀 Recommendations")

for rec in recommendations:
    st.write(f"- {rec}")


# ==============================
# PMO PROJECT STATUS
# ==============================
st.header("📋 Project Status (PMO View)")

project = create_project_status()
st.json(project)


# ==============================
# PROCESS COMPARISON
# ==============================
st.header("🔄 Process Comparison")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Current State")
    st.json(current_process())

with col2:
    st.subheader("Future State")
    st.json(future_process())


# ==============================
# REPORT
# ==============================
st.header("📄 Project Report")

report = generate_report(summary, recommendations)
st.text(report)