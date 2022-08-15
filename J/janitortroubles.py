"""Janitor Troubles"""

# janitortroubles

from math import sqrt

areas = list(map(int, input().split()))
result = 1

for i, val in enumerate(areas):
    result *= sum(areas) / 2 - val

print(sqrt(result))
