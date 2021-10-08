"""Amalgamated Artichokes"""

from sys import stdin
from math import sin, cos

p, a, b, c, d, n = [int(x) for x in stdin.readline().split()]

dif = 0
val = p * (sin(a + b) + cos(c + d) + 2)
for i in range(2, n + 1):
    next_val = p * (sin(a * i + b) + cos(c * i + d) + 2)
    if val < next_val:
        val = next_val
    elif val - next_val > dif:
        dif = val - next_val

print(dif)
