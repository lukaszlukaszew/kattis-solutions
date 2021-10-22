"""Heliocentric"""

case = 1

while True:
    try:
        x, y = map(int, input().split())

        if x + y:
            days, y = 365 - x, y + 365 - x

            while y % 687:
                y += 365
                days += 365
        else:
            days = 0

        print(f"Case {case}: {days}")

        case += 1
    except EOFError:
        break
