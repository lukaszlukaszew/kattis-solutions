"""Sylvester Construction"""

from sys import stdin

cases = int(stdin.readline())

for i in range(cases):
    n, x, y, w, h = [int(x) for x in stdin.readline().split()]
    result = []

    for j in range(h):
        row = []
        for k in range(w):
            num, size, point_x, point_y = 1, 2 * n, x + k, y + j

            while size > 1:
                size /= 2

                if point_x >= size and point_y >= size:
                    num *= -1
                if point_x >= size:
                    point_x -= size
                if point_y >= size:
                    point_y -= size

            row.append(num)
        result.append(row)

    for j in result:
        print(*j)

    if i < cases - 1:
        print()
