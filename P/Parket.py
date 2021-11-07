"""Parket"""

from math import sqrt

R, B = map(int, input().split())

d = (R + 4) ** 2 - 4 * (-2) * (-2 * (R + B))
L = max((-(R + 4) + sqrt(d)) / (-4), (-(R + 4) - sqrt(d)) / (-4))

print(max(int(L), int((R + B) / L)), min(int(L), int((R + B) / L)))
