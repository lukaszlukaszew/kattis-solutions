"""Combination Lock"""

line = [int(x) for x in input().split()]

while sum(line):
    rotation = 1080

    for i in range(3):
        if i == 1:
            diff = line[i + 1] - line[i]
        else:
            diff = line[i] - line[i + 1]

        if diff < 0:
            diff += 40

        rotation += diff * 9

    line = [int(x) for x in input().split()]

    print(rotation)
