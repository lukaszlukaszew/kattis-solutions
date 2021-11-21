"""Safe Houses"""

from sys import stdin

size = int(stdin.readline())
spies, houses = [], []

for i in range(size):
    line = stdin.readline()
    for j in range(size):
        if line[j] == "H":
            houses.append((i, j))
        elif line[j] == "S":
            spies.append((i, j))

global_dist = 0

for i in spies:
    local_dist = float("inf")
    for j in houses:
        local_dist = min(local_dist, abs(i[0] - j[0]) + abs(i[1] - j[1]))
    global_dist = max(global_dist, local_dist)

print(global_dist)
