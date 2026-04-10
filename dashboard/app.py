import streamlit as st
import pandas as pd

st.title("PMO Quality Dashboard")

df = pd.read_csv("../data/raw/shipping_data.csv")

st.write("### Data Overview")
st.dataframe(df)

st.write("### Delay Distribution")
st.bar_chart(df["delay_days"])
