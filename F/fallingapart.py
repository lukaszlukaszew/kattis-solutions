"""Falling Apart"""

# fallingapart

input()
values = sorted(list(map(int, input().split())))
Alice, Bob = 0, 0

while values:
    try:
        Alice += values.pop()
        Bob += values.pop()
    except IndexError:
        break

print(Alice, Bob)
