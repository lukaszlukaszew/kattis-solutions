"""Code Cleanups"""

input()
dates = [int(x) for x in input().split()][::-1]
cleanups, counter, penalty = 0, 0, 0

for i in range(1, 366):
    penalty += counter

    if dates:
        if i == dates[-1]:
            counter += 1
            dates.pop()

    if penalty + counter >= 20:
        penalty, counter = 0, 0
        cleanups += 1

print(cleanups + int(bool(counter)))
