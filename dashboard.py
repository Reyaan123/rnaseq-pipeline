import streamlit as st
import sqlite3
import pandas as pd
conn = sqlite3.connect("pipeline_results.db")
cursor = conn.cursor()
import torch


data = cursor.execute("SELECT * FROM expression_results")
results = cursor.fetchall()
df= pd.DataFrame(results, columns=["gene_name","mean_healthy","mean_cancer", "p_value"])

st.title("RNA-Seq Pipleine Results")
st.subheader("Gene expression comparason")
st.bar_chart(df.set_index("gene_name")[["mean_healthy", "mean_cancer"]])
st.dataframe(results)



st.subheader("Autoencoder Latent Space")

ae_df= pd.DataFrame([[0.7480, 0.8861, 0.4513],
 [0.9201, 1.1470, 0.6421],
 [0.8097, 1.0548, 0.5738],
 [0.9836, 0.9424, 0.7333],
 [0.7780, 0.7878, 0.4659],
 [0.9386, 0.9086, 0.5117],
 [0.8706, 0.9433, 0.5595],
 [0.7906, 0.8639, 0.3823]], columns=["dim1", "dim2","dim3"])

st.dataframe(ae_df)
st.line_chart(ae_df)