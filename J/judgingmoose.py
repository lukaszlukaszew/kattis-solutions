"""Judging Moose"""

# judgingmoose

L, R = map(int, input().split())

if L == R:
    if L:
        print("Even", 2 * L)
    else:
        print("Not a moose")
else:
    print("Odd", max(L, R) * 2)
