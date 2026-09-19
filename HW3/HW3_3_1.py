#Mostly Same as 3_2_1 With exception of line 19
import numpy as np
import matplotlib.pyplot as plt

# Sample size and number of samples
n = 10
num_samples = 10000

# Generate 10,000 samples with 10 values in each sample
samples = np.random.normal(0, 1, size=(num_samples, n))

# Calculate the mean of each sample
xbars = np.mean(samples, axis=1)

# Calculate the average of all sample means
average_xbar = np.mean(xbars)

# Calculate the fraction of sample means above 1/sqrt(n)
fraction = np.mean(xbars > 1 / np.sqrt(n))

# Plot 
plt.hist(xbars, bins=30, density=True)

plt.xlabel('Sample Mean')
plt.ylabel('Probability Density')
plt.title(  f'Distribution of Sample Means\n' f'Average = {average_xbar:.4f}, Fraction Above 1/sqrt(n) = {fraction:.4f}')

plt.savefig('HW3_3_1.png')
plt.show()