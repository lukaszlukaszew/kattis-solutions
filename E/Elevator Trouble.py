"""Elevator Trouble"""

from sys import stdin
from collections import defaultdict, deque

f, s, g, u, d = map(int, stdin.readline().split())

result = True
queue = deque()
queue.append((0, s))
visited = defaultdict(lambda: True)

while queue:
    cost, floor = queue.popleft()

    if floor == g:
        print(cost)
        result = False
        break

    if visited[floor + u] and floor + u <= f:
        queue.append((cost + 1, floor + u))
        visited[floor + u] = False

    if visited[floor - d] and floor - d >= 1:
        queue.append((cost + 1, floor - d))
        visited[floor - d] = False

if result:
    print("use the stairs")
