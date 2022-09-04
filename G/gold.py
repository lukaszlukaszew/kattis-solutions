"""Getting Gold"""

# gold

from collections import deque

X, Y = map(int, input().split())
board, queue, visited = [], deque(), set()
moves = ((-1, 0), (1, 0), (0, 1), (0, -1))
gold = 0

for i in range(Y):
    board.append(list(input()))

    if "P" in board[i]:
        y, x = i, board[i].index("P")
        queue.append((x, y))
        visited.add((x, y))
        board[y][x] = "."

while queue:
    x, y = queue.popleft()

    for i in moves:
        if 0 <= x + i[0] < X and 0 <= y + i[1] < Y:
            if board[y + i[1]][x + i[0]] == "T":
                break
    else:
        for i in moves:
            if 0 <= x + i[0] < X and 0 <= y + i[1] < Y and board[y + i[1]][x + i[0]] != "#":
                if (x + i[0], y + i[1]) not in visited:
                    if board[y + i[1]][x + i[0]] == "G":
                        gold += 1
                        board[y + i[1]][x + i[0]] = "."

                    visited.add((x + i[0], y + i[1]))
                    queue.append((x + i[0], y + i[1]))

print(gold)
