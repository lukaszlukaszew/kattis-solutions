"""Splat"""

# splat

from math import pi

painting_descriptions = int(input())

for i in range(painting_descriptions):
    drop_count = int(input())
    drops = []
    for k in range(drop_count):
        drop = input().split()
        for j in range(3):
            drop[j] = float(drop[j])

        drops.append(drop)

    point_counts = int(input())

    for j in range(point_counts):
        X, Y = map(float, input().split())
        color = "white"
        for k in drops[::-1]:
            if (X - k[0]) ** 2 + (Y - k[1]) ** 2 - (k[2] / pi) <= 0:
                color = k[3]
                break

        print(color)
