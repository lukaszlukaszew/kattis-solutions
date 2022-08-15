"""Bottled-Up Feelings"""

# bottledup

s, v1, v2 = [int(x) for x in input().split()]
x, y = int(s // v1), 0

if s % v1:
    while x >= 0:
        if not (s - x * v1) % v2:
            y = int((s - x * v1) // v2)
            break
        x -= 1

if x * v1 + y * v2 != s:
    print("Impossible")
else:
    print(x, y)
