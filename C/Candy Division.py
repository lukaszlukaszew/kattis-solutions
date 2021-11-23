"""Candy Division"""

from math import sqrt


def divisors(candy):
    """Search for divisors"""
    result = []
    for i in range(1, int(sqrt(candy)) + 1):
        if candy % i == 0:
            result.append(i)
    for i in range(len(result) - 1, -1, -1):
        result.append(candy // result[i])

    return set(result)


print(*[x - 1 for x in sorted(divisors(int(input())))])
