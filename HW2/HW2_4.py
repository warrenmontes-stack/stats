import random
import math
import matplotlib.pyplot as plt

# Given values
n = 100
p = 0.4
q = 1 - p
num_experiments = 10000

# Store the number of successes from each experiment
results = []

# -----------------------------
# Part 1: Simulate 10,000 experiments
# -----------------------------

for experiment in range(num_experiments):

    successes = 0

    # Each experiment contains 100 Bernoulli trials
    for trial in range(n):

        result = random.choices(
            [0, 1],
            weights=[q, p]
        )[0]

        successes += result

    results.append(successes)

# Possible values of x
x_values = list(range(n + 1))

# -----------------------------
# Simulated P(x)
# -----------------------------

simulated_probabilities = []

for x in x_values:

    probability = results.count(x) / num_experiments

    simulated_probabilities.append(probability)

# -----------------------------
# Exact binomial P(x)
# -----------------------------

binomial_probabilities = []

for x in x_values:

    probability = (
        math.comb(n, x)
        * (p ** x)
        * (q ** (n - x))
    )

    binomial_probabilities.append(probability)

# -----------------------------
# Part 2: Large-n approximation
# -----------------------------

approx_probabilities = []

for x in x_values:

    probability = (
        1 / math.sqrt(2 * math.pi * n * p * q)
        * math.exp(
            -((x - n * p) ** 2)
            / (2 * n * p * q)
        )
    )

    approx_probabilities.append(probability)

# -----------------------------
# Plot all three
# -----------------------------

plt.plot(
    x_values,
    simulated_probabilities,
    label="Simulation"
)

plt.plot(
    x_values,
    binomial_probabilities,
    label="Exact Binomial"
)

plt.plot(
    x_values,
    approx_probabilities,
    label="Approximation"
)

plt.xlabel("x")
plt.ylabel("P(x)")
plt.title("Binomial Distribution: n = 100, p = 0.4")

plt.legend()
plt.grid()

plt.savefig("HW2_4.png")

plt.show()
# ---------------------------------------------------------------------
#  AI assistance used to solve this problem without numpy assistance.
# ---------------------------------------------------------------------