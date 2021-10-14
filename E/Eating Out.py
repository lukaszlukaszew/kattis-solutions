"""Eating Out"""

m, a, b, c = [int(x) for x in input().split()]

if m * 2 < a + b + c:
    print("impossible")
else:
    print("possible")
