"""Dirty Driving"""

n, p = [int(x) for x in input().split()]
distances = sorted(map(int, input().split()))
safety = 0

for i in range(n):
    safety = max(safety, p * (i + 1) - distances[i])

print(distances[0] + safety)
