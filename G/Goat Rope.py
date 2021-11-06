"""Goat Rope"""

from math import sqrt

x, y, x1, y1, x2, y2 = map(float, input().split())
result = []

if x1 < x < x2:
    print(min(abs(y1 - y), abs(y2 - y)))
elif y1 < y < y2:
    print(min(abs(x1 - x), abs(x2 - x)))
else:
    result.append(sqrt((x1 - x) ** 2 + (y1 - y) ** 2))
    result.append(sqrt((x1 - x) ** 2 + (y2 - y) ** 2))
    result.append(sqrt((x2 - x) ** 2 + (y1 - y) ** 2))
    result.append(sqrt((x2 - x) ** 2 + (y2 - y) ** 2))
    print(min(result))
