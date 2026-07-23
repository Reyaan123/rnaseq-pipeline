import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect("pipeline_results.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM expression_results")
results = cursor.fetchall()
df = pd.DataFrame(results, columns=["gene_id", "mean_flight", "mean_ground", "log2_fold_change", "t_statistic", "p_value"])

st.title("RNA-Seq Pipeline Results — OSD-635 Spaceflight Data")
st.subheader("Gene expression: Flight vs Ground")
st.bar_chart(df.set_index("gene_id")[["mean_flight", "mean_ground"]])
st.dataframe(df)