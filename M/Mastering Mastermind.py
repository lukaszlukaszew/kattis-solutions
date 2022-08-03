"""Mastering Mastermind"""

# mastermind

n, first, second = input().split()
first, second = list(first), list(second)
r, s = 0, 0

for i, val in enumerate(first):
    if val == second[i]:
        first[i], second[i] = "", ""
        r += 1

for i, val in enumerate(first):
    if val and val in second:
        second[second.index(val)], first[i] = "", ""
        s += 1

print(r, s)
