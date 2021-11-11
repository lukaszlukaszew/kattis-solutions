"""Beehives"""

from math import sqrt

distance, hives_count = map(float, input().split())

while distance + hives_count:
    sour, sweet, hives = 0, 0, []

    for i in range(int(hives_count)):
        hives.append([float(x) for x in input().split()])

    for i in hives:
        x1, y1 = i
        counter = False

        for j in hives:
            x2, y2 = j

            distance_between = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

            if distance_between < float(distance) and distance_between:
                counter = True
                break

        sour += int(counter)
        sweet += int(not counter)

    print(f"{sour} sour, {sweet} sweet")

    distance, hives_count = map(float, input().split())
