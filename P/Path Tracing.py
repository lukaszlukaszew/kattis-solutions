"""Path Tracing"""

from sys import stdin

path = [["S", ], ]
x, y = 0, 0

for direction in stdin:
    if direction.rstrip():
        if direction.rstrip() == "up":
            if y == 0:
                path.insert(0, [" ", ] * len(path[0]))
            else:
                y -= 1
        elif direction.rstrip() == "down":
            if y == len(path) - 1:
                path.append([" ", ] * len(path[0]))
            y += 1
        elif direction.rstrip() == "left":
            if x == 0:
                for i, val in enumerate(path):
                    val.insert(0, " ")
            else:
                x -= 1
        elif direction.rstrip() == "right":
            if x == len(path[0]) - 1:
                for i, val in enumerate(path):
                    val.append(" ")
            x += 1

        if path[y][x] != "S":
            path[y][x] = "*"
    else:
        break

path[y][x] = "E"

for i, val in enumerate(path):
    val.insert(0, "#")
    val.append("#")

path.insert(0, ["#", ] * len(path[0]))
path.append(["#", ] * len(path[0]))

for i in path:
    print("".join(i))
