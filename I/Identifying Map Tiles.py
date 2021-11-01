"""Identifying Map Tiles"""

quadkey = input()
basic = {"0": (0, 0), "1": (1, 0), "2": (0, 1), "3": (1, 1)}
x, y = 0, 0

for i, val in enumerate(quadkey):
    x += 2 ** (len(quadkey) - i - 1) * basic[val][0]
    y += 2 ** (len(quadkey) - i - 1) * basic[val][1]

print(len(quadkey), x, y)
