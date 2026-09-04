import random

steps = [-1, 1]

n = 10000
count = 0

for trial in range(n):
    result = []

    for step in range(3):
        result.append(random.choice(steps))

    final_position = sum(result)

    if final_position == 1:
        count += 1

probability = count / n

print(f"Estimated probability = {probability}")
#AI Used to solve this problem