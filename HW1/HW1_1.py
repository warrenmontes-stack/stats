import random
import matplotlib.pyplot as plt

a = [0, 1]

# Repeat the experiment n times
results = []

# Store values for the graph
n_values = []
rf_values = []

for n in range(1, 1001):
    result = random.choice(a)
    results.append(result)

    # rf = relative frequency of 1
    rf = results.count(1) / n

    n_values.append(n)
    rf_values.append(rf)

    print(f"n = {n} experiments:")
    print(f"  rf(1) = {results.count(1) / n}")

# Plot Rf vs n
plt.plot(n_values, rf_values)
plt.xlabel("n")
plt.ylabel("Rf")
plt.title("Relative Frequency vs. n")
plt.show()