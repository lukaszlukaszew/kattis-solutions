"""Malfunctioning Robot"""

cases = int(input())

for i in range(cases):
    x, y, X, Y = [int(x) for x in input().split()]
    rest = max(abs(x - X), abs(y - Y)) - min(abs(x - X), abs(y - Y))
    print(2 * min(abs(x - X), abs(y - Y)) + (rest - int(rest % 2)) * 2 + int(rest % 2))
