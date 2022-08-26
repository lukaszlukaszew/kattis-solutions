"""Logo"""

# logo

from math import sqrt, cos, sin, radians
from collections import defaultdict

cases = int(input())

for i in range(cases):
    moves = int(input())
    angles, angle = defaultdict(int), 0

    for j in range(moves):
        instr, val = input().split()

        if instr == "fd":
            angles[angle] += int(val)
        elif instr == "lt":
            angle = int((angle + int(val)) % 360)
        elif instr == "rt":
            angle = int(int(360 + angle - int(val)) % 360)
        elif instr == "bk":
            angles[int((180 + angle) % 360)] += int(val)

    x, y = 0, 0

    for k, v in angles.items():
        x += v * cos(radians(k))
        y += v * sin(radians(k))

    print(round(sqrt(x**2 + y**2)))
