"""Patuljci"""

# patuljci

from itertools import combinations

dwarves = []

for i in range(9):
    dwarves.append(int(input()))

for i in combinations(dwarves, 7):
    if sum(i) == 100:
        group = set(i)

for i, val in enumerate(dwarves):
    if val in group:
        print(val)
