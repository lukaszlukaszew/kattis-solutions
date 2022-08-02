"""A List Game"""

# listgame

from math import sqrt

X = int(input())
points = 0


def primes(limit):
    """Primes generator"""
    primes_list = []

    if primes_list:
        z = max(primes_list)
    else:
        z = 1

    for k in range(z + 1, limit + 1):
        for j in primes_list:
            if k % j == 0:
                break
        else:
            yield k
            primes_list.append(k)

    return primes_list


for i in primes(int(sqrt(X)) + 1):
    while X % i == 0:
        points += 1
        X /= i

if X > int(sqrt(X)) + 1:
    points += 1

print(points)
