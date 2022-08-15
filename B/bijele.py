"""Bijele"""

# bijele

found = list(map(int, input().split()))
full = [1, 1, 2, 2, 2, 8]

print(*list(map(lambda x, y: x - y, full, found)))
