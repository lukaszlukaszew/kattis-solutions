"""Fun House"""

# funhouse


def beam(x, y, direction, image):
    """Find full beam path"""
    reflections = {
        (0, 1): {"\\": (1, 0), "/": (-1, 0)},
        (0, -1): {"\\": (-1, 0), "/": (1, 0)},
        (-1, 0): {"\\": (0, -1), "/": (0, 1)},
        (1, 0): {"\\": (0, 1), "/": (0, -1)},
    }

    while True:
        while house[y][x] not in "\\/x":
            x, y = x + direction[0], y + direction[1]

        if image[y][x] == "x":
            image[y][x] = "&"
            return image

        direction = reflections[direction][image[y][x]]
        x, y = x + direction[0], y + direction[1]


counter = 1

while True:
    house = []
    X, Y = [int(x) for x in input().split()]

    if X + Y == 0:
        break

    for i in range(Y):
        line = list(input())

        if "*" in line:
            start = [line.index("*"), i]

        house.append(line)

    if start[1] == 0:
        orientation = (0, 1)
    elif start[1] == Y - 1:
        orientation = (0, -1)
    elif start[0] == 0:
        orientation = (1, 0)
    elif start[0] == X - 1:
        orientation = (-1, 0)

    beam(*start, orientation, house)

    print("HOUSE", counter)

    for row in house:
        print("".join(row))

    counter += 1
