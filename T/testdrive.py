"""Test Drive"""

# testdrive

a, b, c = map(int, input().split())

if b - a == c - b:
    print("cruised")
elif a < b < c or a > b > c:
    if abs(b - a) > abs(c - b):
        print("braked")
    elif abs(b - a) < abs(c - b):
        print("accelerated")
else:
    print("turned")
