"""Ornaments"""

from math import pi, acos, sqrt

r, h, e = [float(x) for x in input().split()]

while r + h + e:
    rounded_part = (2 * pi * r) * (((pi + 2 * (pi / 2 - acos(r / h))) * r) / (2 * pi * r))
    straight_part = 2 * sqrt(h ** 2 - r ** 2)
    print(format((rounded_part + straight_part) * (1 + e / 100), ".2f"))
    r, h, e = [float(x) for x in input().split()]
