"""Rings"""

from sys import stdin

r, c = map(int, stdin.readline().split())

grid, trees, ring = [], set(), 1

for i in range(r):
    grid.append(list(stdin.readline().rstrip()))
    for j in range(c):
        if grid[i][j] == "T":
            trees.add((i, j))

while trees:
    done = set()
    for tree in trees:
        if tree[0] in (0, r - 1) or tree[1] in (0, c - 1):
            grid[tree[0]][tree[1]] = ring
            done.add(tree)
        else:
            for j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                if 0 <= tree[0] + j[0] < r and 0 <= tree[1] + j[1] < c:
                    if (
                        grid[tree[0] + j[0]][tree[1] + j[1]] == ring - 1
                        or grid[tree[0] + j[0]][tree[1] + j[1]] == "."
                    ):
                        grid[tree[0]][tree[1]] = ring
                        done.add(tree)
                        break

    trees = trees.difference(done)
    ring += 1

for i in grid:
    print(
        "".join(
            map(lambda x: ((3 if ring >= 10 else 2) - len(str(x))) * "." + str(x), i)
        )
    )
