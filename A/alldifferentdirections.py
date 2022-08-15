"""All Different Directions"""

# alldifferentdirections

import math

people = int(input())

while people:
    destinations = []
    avgX, avgY, far_off = 0, 0, 0

    for i in range(people):
        instr = input().split()

        X, Y, angle = float(instr[0]), float(instr[1]), float(instr[3])

        instr = instr[4:]

        for j in range(int(len(instr) // 2)):
            if instr[2 * j] == "walk":
                X += float(instr[2 * j + 1]) * math.cos(math.radians(angle))
                Y += float(instr[2 * j + 1]) * math.sin(math.radians(angle))
            else:
                angle += float(instr[2 * j + 1])

        destinations.append((X, Y))
        avgX += X
        avgY += Y

    avgX /= people
    avgY /= people

    for i in range(people):
        far_off = max(
            far_off,
            math.sqrt(
                (avgX - destinations[i][0]) ** 2 + (avgY - destinations[i][1]) ** 2
            ),
        )

    print(avgX, avgY, far_off)
    people = int(input())
