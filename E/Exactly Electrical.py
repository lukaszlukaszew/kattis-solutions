"""Exactly Electrical"""

x1, y1 = [int(x) for x in input().split()]
x2, y2 = [int(x) for x in input().split()]
charge = int(input())
dist = abs(x1 - x2) + abs(y1 - y2)

result = "N"

if charge >= dist and dist % 2 == charge % 2:
    result = "Y"

print(result)
