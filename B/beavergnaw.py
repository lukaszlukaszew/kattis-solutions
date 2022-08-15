"""Beavergnaw"""

# beavergnaw

import math

D, V = map(int, input().split())

while D and V:
    print(math.pow(D ** 3 - (12 * V / (2 * math.pi)), 1 / 3))
    D, V = map(int, input().split())
