"""Vacuumba"""

# vacuumba

from math import sin, cos, radians

cases = int(input())

for i in range(cases):
    segments = int(input())
    x, y, angle = 0, 0, 0

    for j in range(segments):
        turn, distance = [float(x) for x in input().split()]

        angle += turn
        x += distance * sin(-radians(angle))
        y += distance * cos(-radians(angle))

    print(x, y)
