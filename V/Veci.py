"""Veci"""

# veci

from itertools import permutations

number = list(input())

perm = list(
    filter(
        lambda x: x > int("".join(number)),
        map(lambda x: int("".join(x)), (permutations(number, len(number)))),
    )
)
if perm:
    print(min(perm))
else:
    print(0)
