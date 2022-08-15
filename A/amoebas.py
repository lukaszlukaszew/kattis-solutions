"""Sheba's Amoebas"""

# amoebas


def size(x, X, y, Y, dish):
    """Remove full amoeba from petri_dish"""
    dish[y * X + x] = False
    for k in (-1, 0, 1):
        for v in (-1, 0, 1):
            if not k == v == 0:
                x, y = x + k, y + v
                if 0 <= x < X and 0 <= y < Y:
                    if dish[y * X + x]:
                        size(x, X, y, Y, dish)
                x, y = x - k, y - v


R, C = map(int, input().split())
petri_dish, amoebas = [], 0

for r in range(R):
    line = input()
    for char in line:
        petri_dish.append(char == "#")

for r in range(R):
    for c in range(C):
        if petri_dish[r * C + c]:
            amoebas += 1
            size(c, C, r, R, petri_dish)

print(amoebas)
