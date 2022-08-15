"""Sierpiński Circumference"""

# triangle

from sys import stdin

case = 0

while True:
    try:
        n = int(stdin.readline())
        circumference, digits = 3, 1

        for i in range(n):
            circumference *= 1.5
            if circumference > 10:
                circumference /= 10
                digits += 1

        case += 1

        print("Case " + str(case) + ":", digits)
    except ValueError:
        break
