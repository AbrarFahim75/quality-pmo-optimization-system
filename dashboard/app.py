import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd

from src.analytics.kpi_tracker import compute_kpis
from src.analytics.insights import get_insights, generate_summary
from src.process.optimizer import generate_recommendations


# ==============================
# TITLE
# ==============================
st.title("🚢 AI-Powered Maritime Performance Optimization System")


# ==============================
# LOAD DATA
# ==============================
df = pd.read_csv("data/raw/ship_performance.csv")
df = compute_kpis(df)

insights = get_insights(df)
summary = generate_summary(insights)
recommendations = generate_recommendations(summary)


# ==============================
# KEY METRICS
# ==============================
st.header("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Profit", round(df["Profit"].mean(), 2))
col2.metric("Avg Delay", round(df["Turnaround_Time_hours"].mean(), 2))
col3.metric("Avg Efficiency", round(df["Efficiency_nm_per_kWh"].mean(), 2))


# ==============================
# DATA OVERVIEW
# ==============================
st.header("📊 Raw Operational Data")
st.dataframe(df.head())


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