"""Convex Polygon Area"""

vertices = int(input())

for i in range(vertices):
    pairs, *coordinates = map(int, input().split())
    y = [coordinates[x] for x in range(1, len(coordinates), 2)]
    x = [coordinates[x] for x in range(0, len(coordinates), 2)]
    area = 0

    for j in range(pairs):
        try:
            area += (x[j] + x[j + 1]) * (y[j + 1] - y[j])
        except IndexError:
            area += (x[-1] + x[0]) * (y[0] - y[-1])

    print(area / 2)
