"""Kolone"""

# kolone

lt, rt = [int(x) for x in input().split()]

left = list(input())[::-1]
right = list(input())

time = int(input())

while left:
    right.insert(min(rt, time), left.pop())
    time = max(time - 1, 0)

print("".join(right))
