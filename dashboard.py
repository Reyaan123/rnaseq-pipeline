import streamlit as st
import sqlite3
import pandas as pd
conn = sqlite3.connect("pipeline_results.db")
cursor = conn.cursor()

st.title("RNA-Seq Pipleine Results")

data = cursor.execute("SELECT * FROM expression_results")
results = cursor.fetchall()
st.dataframe(results)