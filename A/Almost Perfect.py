"""Almost Perfect"""

from sys import stdin
from math import sqrt


def divisors(x):
    """Serach for all divisors of x"""
    divs = []
    for i in range(1, int(sqrt(x)) + 1):
        if x % i == 0:
            divs.append(i)
    for i in range(len(divs) - 1, 0, -1):
        if x / divs[i] != divs[i]:
            divs.append(num // divs[i])

    return sum(divs)


for line in stdin:
    if line == "\n":
        break

    num = int(line)
    result = divisors(num)

    if result == num:
        note = "perfect"
    elif abs(result - num) <= 2:
        note = "almost perfect"
    else:
        note = "not perfect"

    print(num, note)
