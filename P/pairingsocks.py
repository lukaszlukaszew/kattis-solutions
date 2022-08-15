"""Pairing Socks"""

# pairingsocks

from sys import stdin

socks = int(stdin.readline())
left = stdin.readline().rstrip().split()[::-1]
right, moves = [], 0

while left:
    if right:
        if left[-1] == right[-1]:
            right.pop()
            left.pop()
        else:
            right.append(left.pop())

    else:
        right.append(left.pop())

    moves += 1

if right:
    print("impossible")
else:
    print(moves)
