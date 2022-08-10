"""Curve Speed"""

# curvespeed

while True:
    try:
        R, S = map(float, input().split())
        print(int(round(((R*(S+0.16))/0.067)**(1/2))))
    except EOFError:
        break
