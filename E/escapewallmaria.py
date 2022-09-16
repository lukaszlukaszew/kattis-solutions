"""Escape Wall Maria"""

# escapewallmaria

from sys import stdin
from collections import deque

t, N, M = map(int, stdin.readline().split())

moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
directions = {"U": (1, 0), "D": (-1, 0), "L": (0, 1), "R": (0, -1)}
grid, visited, queue = [], set(), deque()
result = "NOT POSSIBLE"

for i in range(N):
    row = list(stdin.readline().rstrip())
    if "S" in row:
        y, x = i, row.index("S")
        queue.append((0, y, x))
        visited.add((y, x))
    grid.append(row)

while queue:
    current_cost, y, x = queue.popleft()

    if current_cost > t:
        break

    if y in (0, N - 1) or x in (0, M - 1):
        result = current_cost
        break

    for move in moves:
        if 0 <= move[0] + y < N and 0 <= move[1] + x < M and (move[0] + y, move[1] + x) not in visited:
            if grid[move[0] + y][move[1] + x] == "0" or directions.get(grid[move[0] + y][move[1] + x], 0) == move:
                visited.add((move[0] + y, move[1] + x))
                queue.append((current_cost + 1, move[0] + y, move[1] + x))

print(result)
