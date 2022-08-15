"""Greedy Polygons"""

# greedypolygons

import math

cases = int(input())

for i in range(cases):
    n, l, d, g = map(int, input().split())

    area = n * l * d * g + (d * g) ** 2 * math.pi
    area += (n / 4) * (l ** 2) * (1 / (math.tan(math.radians(180 / n))))

    print(area)
