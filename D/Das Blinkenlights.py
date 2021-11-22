"""Das Blinkenlights"""


def nwd(x, y):
    """Greatest common divisor"""
    while y != 0:
        y, x = x % y, y
    return x


def nww(x, y):
    """Least common multiple"""
    return abs(x * y / nwd(x, y))


p, q, s = map(int, input().split())

if nww(p, q) <= s:
    print("yes")
else:
    print("no")
