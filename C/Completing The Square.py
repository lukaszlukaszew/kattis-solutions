"""Completing The Square"""

# completingthesquare

from math import sqrt

[Ax, Ay] = [int(x) for x in input().split()]
[Bx, By] = [int(x) for x in input().split()]
[Cx, Cy] = [int(x) for x in input().split()]
X, Y = 0, 0

if sqrt((Bx - Ax) ** 2 + (By - Ay) ** 2) == sqrt((Bx - Cx) ** 2 + (By - Cy) ** 2):
    X = Cx + Ax - Bx
    Y = Ay + Cy - By
elif sqrt((Cx - Ax) ** 2 + (Cy - Ay) ** 2) == sqrt((Cx - Bx) ** 2 + (Cy - By) ** 2):
    X = Ax + Bx - Cx
    Y = By + Ay - Cy
elif sqrt((Ax - Bx) ** 2 + (Ay - By) ** 2) == sqrt((Ax - Cx) ** 2 + (Ay - Cy) ** 2):
    X = Cx + Bx - Ax
    Y = By + Cy - Ay

print(X, Y)
