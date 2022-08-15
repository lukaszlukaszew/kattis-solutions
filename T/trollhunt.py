"""Troll Hunt"""

# trollhunt

from math import ceil

b, k, g = [int(x) for x in input().split()]
print(ceil((b - 1) / int(k // g)))
