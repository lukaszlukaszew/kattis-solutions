"""Jumbled Compass"""

# compass


def change(x, y):
    """Comparision function"""
    clockwise = y - x + 360 * int(x > y)
    cclockiwse = -(360 - clockwise)

    if abs(clockwise) <= abs(cclockiwse):
        return clockwise

    return cclockiwse


print(change(int(input()), int(input())))
