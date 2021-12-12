"""Parking"""

cases = int(input())

for i in range(cases):
    stores = int(input())
    positions = sorted(map(int, input().split()))

    distance = 0

    for j in range(stores - 1):
        distance += abs(positions[j] - positions[j + 1])

    print(distance + max(positions) - min(positions))
