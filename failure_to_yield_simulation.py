
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Simulate Beta distributions for accident probability
# Before Intervention: Prior estimate based on historical data
# After Intervention: 20% reduction in incident rate simulated by adjusting prior

np.random.seed(42)
before_intervention = np.random.beta(35, 65, 10000)  # Original distribution
after_intervention = np.random.beta(28, 72, 10000)   # Simulate 20% reduction

# Calculate mean values for both distributions
mean_before = np.mean(before_intervention)
mean_after = np.mean(after_intervention)

# Plot histograms with seaborn
plt.figure(figsize=(12, 6))
sns.histplot(before_intervention, bins=50, color='blue', alpha=0.6, label="Before Intervention")
sns.histplot(after_intervention, bins=50, color='green', alpha=0.6, label="After Intervention")

plt.axvline(mean_before, color='red', linestyle='dashed', linewidth=2, label=f"Mean Before: {mean_before:.3f}")
plt.axvline(mean_after, color='orange', linestyle='dashed', linewidth=2, label=f"Mean After: {mean_after:.3f}")

# Step 5: Customize labels and display the chart
plt.title("Impact of Safety Measures on Failure to Yield Accidents")
plt.xlabel("Probability of Failure to Yield Right of Way Accidents")
plt.ylabel("Density")
plt.legend()
plt.tight_layout()
plt.show()
