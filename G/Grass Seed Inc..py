"""Grass Seed Inc."""

cost = float(input())
lawns = int(input())
area = 0

for i in range(lawns):
    width, length = map(float, input().split())
    area += width * length

print(area * cost)
