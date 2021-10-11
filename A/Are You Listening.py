"""Are You Listening?"""

from math import sqrt

cx, cy, devices = [int(x) for x in input().split()]
distances = []

for i in range(devices):
    x, y, r = [int(x) for x in input().split()]
    dist = sqrt((cx - x) ** 2 + (cy - y) ** 2)
    distances.append(dist - r)

distances.sort()

counter = 0
results = []
result = 0

for i in distances:
    if i <= 0:
        if counter == 2:
            break
        counter += 1
    elif i > 0:
        if len(results) == 3 - counter:
            break
        results.append(int(i // 1))

if results:
    result = max(results)

print(result)
