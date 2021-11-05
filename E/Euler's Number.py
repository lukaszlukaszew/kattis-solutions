"""Euler's Number"""

from math import factorial


def euler(x):
    """Formula for 'e'"""
    if x:
        return 1 / factorial(x) + euler(x - 1)

    return 1


n = int(input())

if n >= 16:
    print("2.718281828459")
else:
    print(euler(n))
