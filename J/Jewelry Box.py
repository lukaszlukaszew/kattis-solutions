"""Jewelry Box"""

from math import sqrt

cases = int(input())

for i in range(cases):
    x, y = map(int, input().split())
    size1 = (4 * x + 4 * y - sqrt((4 * x + 4 * y) ** 2 - 4 * x * y * 12)) / 24
    size2 = (4 * x + 4 * y + sqrt((4 * x + 4 * y) ** 2 - 4 * x * y * 12)) / 24

    if size1 < x / 2 and size1 < y / 2:
        result = size1
    elif size2 < x / 2 and size2 < y / 2:
        result = size2

    print((x - 2 * result) * (y - 2 * result) * result)
