import streamlit as st
import sqlite3
import pandas as pd
conn = sqlite3.connect("pipeline_results.db")
cursor = conn.cursor()


data = cursor.execute("SELECT * FROM expression_results")
results = cursor.fetchall()
df= pd.DataFrame(results, columns=["gene_name","mean_healthy","mean_cancer", "p_value"])

st.title("RNA-Seq Pipleine Results")
st.subheader("Gene expression comparason")
st.bar_chart(df.set_index("gene_name")[["mean_healthy", "mean_cancer"]])
st.dataframe(results)
