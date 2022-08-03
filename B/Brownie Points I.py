"""Brownie Points I"""

# browniepoints

from sys import stdin

points_count = int(stdin.readline())

while points_count:
    points = []

    for i in range(points_count):
        points.append([int(x) for x in stdin.readline().split()])

    X, Y = points[int(points_count // 2)]
    Stan, Ollie = 0, 0

    for i in points:
        if (i[0] > X and i[1] > Y) or (i[0] < X and i[1] < Y):
            Stan += 1
        elif (i[0] > X and i[1] < Y) or (i[0] < X and i[1] > Y):
            Ollie += 1

    print(Stan, Ollie)

    points_count = int(stdin.readline())
