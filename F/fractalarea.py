"""Fractal Area"""

# fractalarea

from math import pi

cases = int(input())

for i in range(cases):
    r, n = map(int, input().split())
    area = 0

    for j in range(n):
        if j == 0:
            area += r ** 2
        elif j == 1:
            area += 4 * r ** 2
            circles = 4
        else:
            area += circles * 3 * r ** 2
            circles *= 3

        r /= 2

    print(area * pi)
