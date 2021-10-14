"""Contest Struggles"""

from sys import stdin

n, k = map(int, stdin.readline().split())
d, s = map(int, stdin.readline().split())

x = (d * n - k * s) / (n - k)

if x < 0 or x > 100:
    print("impossible")
else:
    print(x)
