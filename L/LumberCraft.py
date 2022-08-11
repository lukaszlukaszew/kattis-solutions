"""LumberCraft"""

# lumbercraft

from string import ascii_uppercase
from collections import Counter, defaultdict

while True:
    turns, h, w = map(int, input().split())

    if turns == h == w == 0:
        break

    maps, trees, mills, wood = [], set(), {}, {}
    order = defaultdict(list)

    for i in range(h):
        row = list(input())
        for j, val in enumerate(row):
            if val == "!":
                trees.add((i, j))
            elif val in ascii_uppercase:
                mills[val] = (i, j)
                wood[val] = 0

        maps.append(row)

    for k, v in mills.items():
        for tree in trees:
            order[k].append(((abs(v[0] - tree[0]) ** 2 + abs(v[1] - tree[1]) ** 2) ** 1 / 2, tree[0], tree[1]))

        order[k] = sorted(order[k], key=lambda x: (-x[0], x[2], x[1]))

    for t in range(turns):
        chosen, to_cut = {}, Counter()
        for k, v in mills.items():
            while order[k]:
                cost, i, j = order[k].pop()
                if (i, j) in trees:
                    chosen[k] = (i, j)
                    to_cut[(i, j)] += 1
                    break

        for k, v in chosen.items():
            wood[k] += 1 / to_cut[v]

        to_cut = set(to_cut.keys())

        for tree in to_cut:
            maps[tree[0]][tree[1]] = "."

        trees = trees.difference(to_cut)

    for row in maps:
        print(*row, sep="")

    for k in sorted(wood.keys()):
        print(k, wood[k])
