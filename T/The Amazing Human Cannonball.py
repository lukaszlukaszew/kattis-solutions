"""The Amazing Human Cannonball"""

from math import tan, radians, cos

cases = int(input())

for i in range(cases):
    v, angle, x, h1, h2 = map(float, input().split())
    y = x * tan(radians(angle)) - (9.81 / 2) * (x / v / cos(radians(angle))) ** 2

    if h1 + 1 <= y <= h2 - 1:
        print("Safe")
    else:
        print("Not safe")
