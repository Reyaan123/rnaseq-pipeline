import sqlite3
import pandas as pd

df = pd.read_csv("significant_genes.csv")

conn = sqlite3.connect("pipeline_results.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS expression_results")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expression_results(
    gene_id TEXT,
    mean_flight REAL,
    mean_ground REAL,
    log2_fold_change REAL,
    t_statistic REAL,
    p_value REAL
    )
""")

for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO expression_results (gene_id, mean_flight, mean_ground, log2_fold_change, t_statistic, p_value) VALUES (?, ?, ?, ?, ?, ?)",
        (row["gene_id"], row.get("mean_flight", None), row.get("mean_ground", None),
         row["log2_fold_change"], row["t_statistic"], row["p_value"])
    )

conn.commit()
print(f"Inserted {len(df)} significant genes into pipeline_results.db")
conn.close()