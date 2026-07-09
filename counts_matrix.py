# Counts matrix: genes x samples
# Rows = genes, Columns = samples (healthy1, healthy2, cancer1, cancer2)
import math
from scipy import stats
counts = {
    "GeneA": [2, 3, 8, 9],
    "GeneB": [5, 4, 2, 1],
    "GeneC": [4, 4, 4, 5],
}

samples = ["healthy1", "healthy2", "cancer1", "cancer2"]

# Calculate total counts per sample
totals = [0, 0, 0, 0]
for gene, values in counts.items():
    for i, val in enumerate(values):
        totals[i] += val

print("Sample totals:", totals)
# Normalize: divide each count by sample total, multiply by 1,000,000 (CPM)
print("\nNormalized counts (CPM):")
print(f"{'Gene':<10}", end="")
for s in samples:
    print(f"{s:>12}", end="")
print()

for gene, values in counts.items():
    print(f"{gene:<10}", end="")
    for i, val in enumerate(values):
        cpm = (val / totals[i]) * 1_000_000
        print(f"{cpm:>12.1f}", end="")
    print()

    

# Log2 transform the CPM values
print("\nLog2 CPM values:")
print(f"{'Gene':<10}", end="")
for s in samples:
    print(f"{s:>12}", end="")
print()

for gene, values in counts.items():
    print(f"{gene:<10}", end="")
    for i, val in enumerate(values):
        cpm = (val / totals[i]) * 1_000_000
        log2cpm = math.log2(cpm + 1)
        print(f"{log2cpm:>12.2f}", end="")
    print() 


# Statistical testing: t-test between healthy and cancer
print("\nDifferential expression results:")
print(f"{'Gene':<10} {'mean_healthy':>14} {'mean_cancer':>12} {'p-value':>10}")
for gene, values in counts.items():
    healthy_vals= [values[0], values[1]]
    cancer_vals = [values[2], values[3]]

    healthy_cpm = [(v / totals[i]) * 1_000_000 for i, v in enumerate(healthy_vals)]
    cancer_cpm = [(v / totals[i+2]) * 1_000_000 for i, v in enumerate(cancer_vals)]
    t_stat, p_value = stats.ttest_ind(healthy_cpm, cancer_cpm)
    
    print(f"{gene:<10} {sum(healthy_cpm)/len(healthy_cpm):>14.1f} {sum(cancer_cpm)/len(cancer_cpm):>12.1f} {p_value:>10.4f}")