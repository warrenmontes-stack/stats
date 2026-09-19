import numpy as np
import matplotlib.pyplot as plt
import math

# Days, Hours, and Flares
d = 1000
h = 24
fl = 900


# Simulation of 1000 days of solar flares

p = fl/(d*h)                                  # Probability of a flare in an hour
data = np.random.binomial(1, p, size=(d, h))  # Simulate each hour
flares_per_day = np.sum(data, axis=1)         # Count flares per day

counts = np.bincount(flares_per_day)          # Count how many days had 0, 1, 2, ... flares
Ps = counts / d                               # Convert counts to probabilities
x = np.arange(len(counts))                    # Creating X Values for the plot

#-------Distributions-------
# Poisson Dist

lamt = fl / d  # Expected number of flares per day

Pp = []

for xi in x:
    Pp.append((lamt**xi * math.exp(-lamt)) / math.factorial(xi))

# Binomial Dist

Pb = []

for xi in x:
    Pb.append(math.comb(h, xi) * p**xi * (1-p)**(h-xi))

# Plot
plt.plot(x, Ps, 'o-', label='Simulation')
plt.plot(x, Pp, 's-', label='Poisson')
plt.plot(x, Pb, '^-', label='Binomial')

plt.xlabel('Number of Flares per Day (x)')
plt.ylabel('Probability P(x)')
plt.title('Simulated, Poisson, and Binomial Flare Distributions')
plt.legend()

plt.show()

# Time Between Flares

hourly_data = data.flatten()
flare_hours = np.where(hourly_data == 1)[0]
time_between_flares = np.diff(flare_hours)

# Histogram

plt.figure()

plt.hist(time_between_flares, bins=30)

plt.xlabel('Time Between Flares (hours)')
plt.ylabel('Frequency')
plt.title('Time Between Simulated Solar Flares')

plt.show()