"""Sibice"""

# sibice

from math import sqrt

N, W, H = map(int, input().split())

for j in range(N):
    length = int(input())
    if length <= sqrt(W ** 2 + H ** 2):
        print("DA")
    else:
        print("NE")
