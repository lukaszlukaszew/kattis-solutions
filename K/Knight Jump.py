"""Knight Jump"""

from collections import deque

size = int(input())
board, moves, visited = [], deque(), set()
jumps = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2))

for i in range(size):
    row = list(input())
    if "K" in row:
        moves.append((row.index("K"), i, 0))
        visited.add((row.index("K"), i))
    board.append(row)


while moves:
    x, y, cost = moves.popleft()

    if x == 0 and y == 0:
        print(cost)
        break

    for i in jumps:
        X, Y = x + i[0], y + i[1]
        if (
            0 <= X < size
            and 0 <= Y < size
            and board[Y][X] != "#"
            and (X, Y) not in visited
        ):
            visited.add((X, Y))
            moves.append((X, Y, cost + 1))

else:
    print(-1)
