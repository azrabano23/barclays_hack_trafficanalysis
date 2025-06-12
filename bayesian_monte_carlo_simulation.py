
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import beta

# Set random seed for reproducibility
np.random.seed(42)

# Step 1: Prior distribution (before intervention)
# Assume a Beta distribution with alpha and beta shaped around a mean of 0.39
alpha_prior = 75
beta_prior = 117  # mean = 75 / (75 + 117) ≈ 0.39

# Generate Monte Carlo samples (before intervention)
samples_before = np.random.beta(alpha_prior, beta_prior, size=10000)

# Step 2: Assume a 20% reduction in failure-to-yield probability
# We simulate the intervention effect by scaling each sample
reduction_factor = 0.80  # 20% reduction
samples_after = samples_before * reduction_factor

# Step 3: Plot the distributions
plt.figure(figsize=(10, 6))

# Histogram after intervention
sns.histplot(samples_after, bins=50, kde=False, color='green', label='Posterior After Intervention', stat='density')

# Histogram before intervention
sns.histplot(samples_before, bins=50, kde=False, color='blue', label='Posterior Before Intervention', stat='density')

# Plot vertical lines for means
mean_before = np.mean(samples_before)
mean_after = np.mean(samples_after)

plt.axvline(mean_before, color='red', linestyle='--', linewidth=2, label=f'Mean Before: {mean_before:.3f}')
plt.axvline(mean_after, color='orange', linestyle='--', linewidth=2, label=f'Mean After: {mean_after:.3f}')

# Labels and legend
plt.title('Updated Probability Distribution for Failure to Yield Right of Way (With Intervention)')
plt.xlabel('Probability of Failure to Yield Right of Way in Accidents')
plt.ylabel('Density')
plt.legend()
plt.tight_layout()
plt.show()
