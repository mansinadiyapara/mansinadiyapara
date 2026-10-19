import numpy as np

np.random.seed(42)

temperatures = np.random.normal(
    loc=70,
    scale=5,
    size=5000
)

# Add repeated values
temperatures[:10] = 70

# Add missing values
temperatures[10:15] = np.nan

# Add unusually large values
temperatures[15:18] = [150, 180, 200]

# Add unusually small values
temperatures[18:20] = [-50, -100]

# Add an invalid sensor error code
temperatures[20] = -999

# Identify missing readings
missing_count = np.isnan(temperatures).sum()

# Keep only finite readings
finite_values = temperatures[np.isfinite(temperatures)]

# Identify invalid readings outside the assumed range
invalid_mask = (
    (finite_values < 0) |
    (finite_values > 120)
)

invalid_count = invalid_mask.sum()

# Keep valid readings
valid = finite_values[~invalid_mask]

# Calculate statistics
print("\n--- Dataset Investigation ---")
print("Total readings:", len(temperatures))
print("Missing readings:", missing_count)
print("Invalid readings:", invalid_count)
print("Valid readings:", len(valid))

print("\nMinimum:", np.min(valid))
print("Maximum:", np.max(valid))
print("Average:", np.mean(valid))
print("Median:", np.median(valid))
print("Standard deviation:", np.std(valid))

print("\n25th percentile:", np.percentile(valid, 25))
print("50th percentile:", np.percentile(valid, 50))
print("75th percentile:", np.percentile(valid, 75))

values, counts = np.unique(valid, return_counts=True)

# Find values that occur more than once
repeated_mask = counts > 1

print("Repeated values:")
print(values[repeated_mask])

print("Their frequencies:")
print(counts[repeated_mask])


# Dataset A: readings are close together
dataset_a = np.array([68, 70, 71, 72, 73, 74, 76])

# Dataset B: readings include extreme values
dataset_b = np.array([20, 25, 30, 35, 40, 100, 254])

# Dataset C: readings have a high concentration around 72
dataset_c = np.array([70, 71, 72, 72, 72, 73, 74])

datasets = {
    "Dataset A": dataset_a,
    "Dataset B": dataset_b,
    "Dataset C": dataset_c,
}

for name, data in datasets.items():
    print(f"\n--- {name} ---")
    print("Readings:", data,name)
    print("Mean:", np.mean(data))
    print("Median:", np.median(data))
    print("Standard deviation:", np.std(data))
    print("Minimum:", np.min(data))
    print("Maximum:", np.max(data))
    print("25th percentile:", np.percentile(data, 25))
    print("75th percentile:", np.percentile(data, 75))
