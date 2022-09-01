"""Misa"""

# misa

from collections import deque


def check(container):
    """Check if handshake is possible"""
    y, x = container.popleft()
    counter = 0
    for seat in taken:
        if abs(y - seat[0]) <= 1 and abs(x - seat[1]) <= 1:
            counter += 1

    return counter


empty, taken = deque(), deque()

Y, X = map(int, input().split())
shakes = 0

for i in range(Y):
    row = list(input())
    for j in range(X):
        if row[j] == ".":
            empty.append((i, j))
        else:
            taken.append((i, j))

while empty:
    shakes = max(shakes, check(empty))

while taken:
    shakes += check(taken)

print(shakes)
