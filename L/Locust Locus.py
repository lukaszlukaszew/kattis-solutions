"""Locust Locus"""

# locustlocus

import sys


def nwd(m, n):
    """Find greatest common divisor"""
    if n > 0:
        return nwd(n, m % n)
    return m


def nww(m, n):
    """Find lowest common multiple"""
    return m * n // nwd(m, n)


pairs = int(input())
year = sys.maxsize

for i in range(pairs):
    y, a, b = map(int, input().split())
    year = min(year, y + nww(a, b))

print(year)
