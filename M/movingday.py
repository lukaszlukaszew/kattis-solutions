"""Moving Day"""

# movingday

boxes, V = [int(x) for x in input().split()]

for i in range(boxes):
    x, y, z = [int(x) for x in input().split()]
    if not i:
        result = x * y * z - V

    result = max(result, x * y * z - V)

print(result)
