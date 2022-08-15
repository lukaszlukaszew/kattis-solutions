"""Dog & Gopher"""

# doggopher

from sys import stdin
from math import sqrt

g_x, g_y, d_x, d_y = map(float, input().split())
holes, result = [], 0

for line in stdin.readlines():
    if line != "\n":
        holes.append(tuple(map(float, line.split())))
    else:
        break

for (x, y) in holes:
    dog = sqrt((x - d_x) ** 2 + (y - d_y) ** 2)
    gopher = sqrt((x - g_x) ** 2 + (y - g_y) ** 2)

    if dog > 2 * gopher:
        print(f"The gopher can escape through the hole at ({x},{y}).")
        break
else:
    print("The gopher cannot escape.")
