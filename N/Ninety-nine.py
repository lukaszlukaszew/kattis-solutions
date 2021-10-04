"""Ninety-nine"""

X = 1

while X < 99:
    print(X)
    X = int(input())
    X += min(3 - (X % 3), 2)

print(99)
