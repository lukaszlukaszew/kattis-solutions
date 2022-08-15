"""Lawn Mower"""

# lawnmower

while True:
    y, x, width = map(float, input().split())

    if y + x + width:
        left, up = 0, 0

        Y = sorted([float(x) for x in input().split()])
        X = sorted([float(x) for x in input().split()])

        for i in X:
            if left >= i - width / 2:
                left = i + width / 2

        for i in Y:
            if up >= i - width / 2:
                up = i + width / 2

        print(["YES", "NO"][int(int(left < 100) + int(up < 75) > 0)])

    else:
        break
