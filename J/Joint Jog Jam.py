"""Joint Jog Jam"""

from math import sqrt

xsk, ysk, xso, yso, xek, yek, xeo, yeo = map(int, input().split())
print(
    max(
        sqrt((xsk - xso) ** 2 + (ysk - yso) ** 2),
        sqrt((xek - xeo) ** 2 + (yek - yeo) ** 2),
    )
)
