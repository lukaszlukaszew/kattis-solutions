"""Fountain"""

from collections import deque

r, c = [int(x) for x in input().split()]
shape, queue, visited = [], deque(), set()

for i in range(r):
    shape.append(list(input()))
    for j in range(c):
        if shape[i][j] == "V":
            queue.append((i, j))

shape.append(
    [
        ".",
    ]
    * c
)

while queue:
    i, j = queue.popleft()
    visited.add((i, j))

    if shape[i + 1][j] == ".":
        shape[i + 1][j] = "V"
        if (i + 1, j) not in visited and i + 1 < r:
            queue.append((i + 1, j))
    elif shape[i + 1][j] == "#":
        for k in (-1, 1):
            if 0 <= j + k < c:
                if shape[i][j + k] == ".":
                    shape[i][j + k] = "V"
                    if (i, j + k) not in visited:
                        queue.append((i, j + k))

for i in range(r):
    print("".join(shape[i]))
