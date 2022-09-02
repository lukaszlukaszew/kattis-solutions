"""Track Smoothing"""

# tracksmoothing

from math import pi, sqrt
from sys import stdin

cases = int(stdin.readline())

for i in range(cases):
    points = []
    radius, points_num = map(int, stdin.readline().split())

    for j in range(points_num):
        points.append(([int(x) for x in stdin.readline().split()]))

    dist = sqrt((points[0][0] - points[-1][0]) ** 2 + (points[0][1] - points[-1][1]) ** 2)

    for j in range(points_num - 1):
        dist += sqrt((points[j][0] - points[j + 1][0]) ** 2 + (points[j][1] - points[j + 1][1]) ** 2)

    scale = (dist - 2 * pi * radius) / dist

    if scale < 0:
        print("Not possible")
    else:
        print(scale)
