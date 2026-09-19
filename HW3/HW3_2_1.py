import numpy as np
import matplotlib.pyplot as plt

# Sample size and number of samples
n = 100
num_samples = 10000

# Generate 10,000 samples with 100 values in each sample
samples = np.random.normal(0, 1, size=(num_samples, n))

# Calculate the mean of each sample
xbars = np.mean(samples, axis=1)

# Calculate the average of all sample means
average_xbar = np.mean(xbars)

# Plot 
plt.hist(xbars, bins=30, density=True)

plt.xlabel('Sample Mean')
plt.ylabel('Probability Density')
plt.title(f'Distribution of Sample Means, Average = {average_xbar:.4f}')

plt.savefig('HW3_2_1.png')
plt.show()