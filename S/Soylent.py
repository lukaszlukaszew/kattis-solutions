"""Soylent"""

# soylent

import math

cases = int(input())

for i in range(cases):
    print(int(math.ceil(int(input()) / 400)))
