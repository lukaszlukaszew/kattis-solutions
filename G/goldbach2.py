"""Goldbach's Conjecture"""

# goldbach2

from sys import stdin


def sieve(n):
    """Sieve for prime numbers"""
    numbers = [True for _ in range(n + 1)]
    result = []
    p = 2

    while p**2 <= n:
        for k in range(p**2, n + 1, p):
            numbers[k] = False
        p += 1

    for p in range(2, n):
        if numbers[p]:
            result.append(p)

    return result


primes = sieve(32000)

cases = int(stdin.readline())

for i in range(cases):
    num = int(stdin.readline())
    representations = []

    for prime in primes:
        if prime < num / 2 + 1:
            if num - prime in primes:
                representations.append(prime)
        else:
            break

    if i:
        print()

    print(f"{num} has {len(representations)} representation(s)")
    for j in representations:
        print(f"{j}+{num-j}")
