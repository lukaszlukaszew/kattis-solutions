"""Costume Contest"""

# costumecontest

from collections import defaultdict

colleagues = int(input())
costumes = defaultdict(int)

for i in range(colleagues):
    costumes[input()] += 1

best = min(costumes.values())

for i in sorted(costumes.keys()):
    if costumes[i] == best:
        print(i)
