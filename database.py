import sqlite3
conn = sqlite3.connect("pipeline_results.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS expression_results")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expression_results(
    gene_name TEXT,
    mean_healthy REAL,
    mean_cancer REAL,
    p_value REAL
    )
""")
cursor.execute ("INSERT INTO expression_results (gene_name, mean_healthy, mean_cancer, p_value) VALUES (?, ?, ?, ?)", ("GeneA", 227272.7, 585714.3, 0.0172))
                                
cursor.execute ("INSERT INTO expression_results (gene_name, mean_healthy, mean_cancer, p_value) VALUES (?, ?, ?, ?)", ("GeneB", 409090.9, 104761.9,0.0359))

conn.commit()

cursor.execute("SELeCT * FROM expression_results")
results = cursor.fetchall()
print (results)