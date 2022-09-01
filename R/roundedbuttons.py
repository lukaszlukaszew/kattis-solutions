"""Rounded Buttons"""

# roundedbuttons

from sys import stdin

result_to_print = {True: "inside", False: "outside"}


def check(x, y, w, h, r, po):
    """Check if point is inside rounded rectangle"""
    for p in range(len(po) // 2):
        result = False
        if x <= po[2 * p + 0] <= x + w and y <= po[2 * p + 1] <= y + h:
            result = True

        if result:
            if po[2 * p + 0] < x + r or po[2 * p + 0] > x + w - r:
                if po[2 * p + 1] < y + r or po[2 * p + 1] > y + h - r:
                    result = False

        if not result:
            circles = [
                (po[2 * p + 0] - (x + r)) ** 2 + (po[2 * p + 1] - (y + r)) ** 2 <= r**2,
                (po[2 * p + 0] - (x + r)) ** 2 + (po[2 * p + 1] - (y + h - r)) ** 2 <= r**2,
                (po[2 * p + 0] - (x + w - r)) ** 2 + (po[2 * p + 1] - (y + h - r)) ** 2 <= r**2,
                (po[2 * p + 0] - (x + w - r)) ** 2 + (po[2 * p + 1] - (y + r)) ** 2 <= r**2,
            ]

            if any(circles):
                result = True

        print(result_to_print[result])


cases = int(stdin.readline())

for j in range(cases):
    X, Y, W, H, R, point_count, *points = (float(x) for x in stdin.readline().split())
    check(X, Y, W, H, R, points)
    print()
