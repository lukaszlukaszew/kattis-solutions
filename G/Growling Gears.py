"""Growling Gears"""

cases = int(input())

for i in range(cases):
    parabolas_count = int(input())
    maximums = []

    for j in range(parabolas_count):
        a, b, c = [int(x) for x in input().split()]
        maximums.append(-(b ** 2 - 4 * (-a) * c) / (4 * (-a)))

    print(maximums.index(max(maximums)) + 1)
