"""Mravi"""

from sys import stdin

N = int(stdin.readline())

normal, lamron, result = {}, {}, {}

for i in range(N - 1):
    line = [int(x) for x in stdin.readline().split()]

    normal[line[0]] = normal.get(line[0], {})
    normal[line[0]][line[1]] = [line[2], line[3]]
    lamron[line[1]] = line[0]

line = [int(x) for x in stdin.readline().split()]

for i in range(N):
    if line[i] != -1:
        result[i + 1] = line[i]

keys_to_check = list(result.keys())
keys_to_check.sort(reverse=True)

for i in keys_to_check:
    child = i
    parent = lamron.get(child, 0)
    while parent != 0:
        amounts = []
        for j in normal[parent].keys():
            amounts.append(
                result.get(j, 0) ** (1 - 1 / 2 * normal[parent][j][1])
                / (normal[parent][j][0] / 100)
            )

        result[parent] = max(amounts)
        child = parent
        parent = lamron.get(child, 0)

print(result.get(1, 0))
