import math
import pandas as pd
import numpy as np
from scipy import stats

def benjamini_hochberg(pvals):
    pvals = np.asarray(pvals)
    n = len(pvals)
    order = np.argsort(pvals)
    ranked = pvals[order]
    bh = ranked * n / np.arange(1, n + 1)
    bh_sorted = np.minimum.accumulate(bh[::-1])[::-1]
    bh_final = np.empty(n)
    bh_final[order] = np.clip(bh_sorted, 0, 1)
    return bh_final

df = pd.read_csv("GLDS-608_rna_seq_Normalized_Counts_rRNArm_GLbulkRNAseq.csv")
df = df.rename(columns={"Unnamed: 0": "gene_id"})

flight_cols = ["SMC-F-E1_S1", "SMC-F-E2_S2", "SMC-F-E3_S3"]
ground_cols = ["SMC-G-E1_S5", "SMC-G-E2_S6", "SMC-G-E3_S7"]

df[flight_cols + ground_cols] = df[flight_cols + ground_cols].apply(
    lambda x: x.apply(lambda v: math.log2(v + 1))
)

def ttest_row(row):
    flight_vals = row[flight_cols].astype(float)
    ground_vals = row[ground_cols].astype(float)
    t_stat, p_value = stats.ttest_ind(flight_vals, ground_vals, equal_var=False)
    return pd.Series({"t_statistic": t_stat, "p_value": p_value})

df[["t_statistic", "p_value"]] = df.apply(ttest_row, axis=1)

df["log2_fold_change"] = df[flight_cols].mean(axis=1) - df[ground_cols].mean(axis=1)
df["mean_flight"] = df[flight_cols].mean(axis=1)
df["mean_ground"] = df[ground_cols].mean(axis=1)

df = df.dropna(subset=["p_value"])

df["fdr_bh"] = benjamini_hochberg(df["p_value"].values)

df_sorted = df.sort_values("p_value")
significant_raw = df_sorted[df_sorted["p_value"] < 0.05]
significant_fdr = df_sorted[df_sorted["fdr_bh"] < 0.05]

print(f"Total genes tested: {len(df)}")
print(f"Significant genes (raw p < 0.05): {len(significant_raw)}")
print(f"Significant genes (FDR-corrected < 0.05): {len(significant_fdr)}")
print("\nTop 10 by p-value:")
print(df_sorted[["gene_id", "log2_fold_change", "t_statistic", "p_value", "fdr_bh"]].head(10))

df_sorted.to_csv("differential_expression_results.csv", index=False)
significant_fdr.to_csv("significant_genes.csv", index=False)
print("\nSaved: differential_expression_results.csv, significant_genes.csv")