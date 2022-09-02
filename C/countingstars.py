"""Counting Stars"""

# countingstars

from sys import stdin
from collections import deque

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
counter = 1

size = stdin.readline().rstrip().split()

while size:
    X, Y, stars, sky = int(size[1]), int(size[0]), 0, []

    for i in range(Y):
        sky.append(list(stdin.readline()))

    for i in range(Y):
        for j in range(X):
            if sky[i][j] == "-":
                stars += 1
                move = deque()
                move.append((i, j))
                sky[i][j] = "#"

                while move:
                    y, x = move.popleft()
                    for v in directions:
                        if 0 <= x + v[0] < X and 0 <= y + v[1] < Y and sky[y + v[1]][x + v[0]] == "-":
                            move.append((y + v[1], x + v[0]))
                            sky[y + v[1]][x + v[0]] = "#"

    print("Case " + str(counter) + ":", stars)
    counter += 1
    size = stdin.readline().rstrip().split()
