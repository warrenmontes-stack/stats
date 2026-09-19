import numpy as np
import matplotlib.pyplot as plt

# Sample size and number of samples
n = 10
num_samples = 10000

# Generate 10,000 samples with 10 values in each sample
samples = np.random.normal(0, 1, size=(num_samples, n))

# Calculate the biased variance of each sample
Sb2 = np.var(samples, axis=1)

# Calculate the average and variance of the 10,000 Sb^2 values
average_Sb2 = np.mean(Sb2)
variance_Sb2 = np.var(Sb2)

# Plot probability density histogram
plt.hist(Sb2, bins=30, density=True)

plt.xlabel('Sample Variance (Sb^2)')
plt.ylabel('Probability Density')
plt.title(  f'Distribution of Sample Variances\n'  f'Average = {average_Sb2:.4f}, Variance = {variance_Sb2:.4f}')

plt.savefig('HW3_3_2.png')
plt.show()