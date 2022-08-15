"""Trik"""

# trik

line = input()
moves = {"A": {3: 3, 1: 2, 2: 1}, "B": {1: 1, 2: 3, 3: 2}, "C": {2: 2, 1: 3, 3: 1}}
cup = 1

for i in line:
    cup = moves[i][cup]

print(cup)
