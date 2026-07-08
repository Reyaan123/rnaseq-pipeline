# Counts matrix: genes x samples
# Rows = genes, Columns = samples (healthy1, healthy2, cancer1, cancer2)

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

    import math

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