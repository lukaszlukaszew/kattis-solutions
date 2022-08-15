"""Planting Trees"""

# plantingtrees

seedlings = int(input())
times = list(sorted(map(int, input().split()), reverse=True))

print(max([x + times[x] + 2 for x in range(seedlings)]))
