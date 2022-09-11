"""Three Powers"""

# threepowers

base = [2**i for i in range(65)]


def next_number(previous):
    """Calculate next number"""
    exponent = base.index([x for x in base if x < previous][-1])
    return previous - 2**exponent, 3**exponent


rest = int(input())

while rest:
    result = []

    while rest > 1:
        rest, num = next_number(rest)
        result.append(num)

    result.sort()
    line = ", ".join(map(str, result))

    print("{" + " " * int(bool(result)) + line + " }")
    rest = int(input())
