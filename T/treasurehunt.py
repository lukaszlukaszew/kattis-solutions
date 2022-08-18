"""Treasure Hunt"""

# treasurehunt

from collections import deque

R, C = [int(x) for x in input().split()]
moves = {"W": (0, -1), "E": (0, 1), "S": (1, 0), "N": (-1, 0)}
visited, board, queue = set(), [], deque()
start, cost = (0, 0), 0

for i in range(R):
    board.append(list(input()))

queue.append((start, cost))
visited.add(start)

while queue:
    (x, y), cost = queue.popleft()

    if x < 0 or x >= C or y < 0 or y >= R:
        print("Out")
        break

    if board[y][x] == "T":
        print(cost)
        break

    if (x + moves[board[y][x]][1], y + moves[board[y][x]][0]) not in visited:
        queue.append(((x + moves[board[y][x]][1], y + moves[board[y][x]][0]), cost + 1))
        visited.add((x, y))

else:
    print("Lost")
