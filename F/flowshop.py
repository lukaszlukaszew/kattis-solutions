"""Flow Shop"""

# flowshop

from sys import stdin

r, c = [int(x) for x in stdin.readline().split()]
machines, result = [], []

for i in range(r):
    machines.append([int(x) for x in stdin.readline().split()])

result.append(sum(machines[0]))

for i in range(1, r):
    machines[i][0] = machines[i - 1][0] + machines[i][0]

for i in range(1, c):
    machines[0][i] = machines[0][i - 1] + machines[0][i]

for i in range(1, r):
    for j in range(1, c):
        machines[i][j] = max(machines[i - 1][j], machines[i][j - 1]) + machines[i][j]
    result.append(machines[i][-1])

print(*result)
