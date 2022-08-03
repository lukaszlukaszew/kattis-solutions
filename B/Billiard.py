"""Billiard"""

# billiard

from math import sqrt, degrees, acos

line = [int(x) for x in input().split()]

while sum(line):
    a, b, s, m, n = line

    x, y = a * m, b * n
    distance = sqrt(x ** 2 + y ** 2)
    v = distance / s
    angle = degrees(acos(x / distance))

    print(f"{angle:.2f} {v:.2f}")

    line = [int(x) for x in input().split()]
