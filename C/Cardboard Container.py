"""Cardboard Container"""

from itertools import combinations_with_replacement
from math import sqrt
from sys import maxsize


def divisors(v):
    """Search for divisors"""
    result = []
    for j in range(1, int(sqrt(v)) + 1):
        if v % j == 0:
            result.append(j)
    for j in range(len(result) - 1, -1, -1):
        result.append(v // result[j])

    return set(result)


V = int(input())
price = maxsize

for i in combinations_with_replacement(divisors(V), 3):
    if i[0] * i[1] * i[2] == V:
        price = min(price, 2 * (i[0] * i[1] + i[0] * i[2] + i[1] * i[2]))

print(price)
