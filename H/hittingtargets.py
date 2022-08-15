"""Hitting the Targets"""

# hittingtargets

from collections import defaultdict

a = int(input())

areas = defaultdict(list)
shots = []

for i in range(a):
    shape, *values = input().split()
    areas[shape].append(tuple(map(int, values)))

s = int(input())

for i in range(s):
    shots.append(tuple(map(int, input().split())))

for shot in shots:
    counter = 0
    for area in areas["circle"]:
        if (shot[0] - area[0]) ** 2 + (shot[1] - area[1]) ** 2 <= area[2] ** 2:
            counter += 1

    for area in areas["rectangle"]:
        if (area[0] <= shot[0] <= area[2]) and (area[1] <= shot[1] <= area[3]):
            counter += 1

    print(counter)
