"""2048"""

# 2048


def prepare_board(b, m):
    """Switch board to make move or produce result"""
    new_board = []

    if m == 0:
        new_board = b
    if m == 1:
        for x in range(3, -1, -1):
            row = []
            for y in range(4):
                row.append(b[y][x])
            new_board.append(row)

    elif m == 2:
        for x in range(4):
            new_board.append(b[x][::-1])

    elif m == 3:
        for x in range(4):
            row = []
            for y in range(3, -1, -1):
                row.append(b[y][x])
            new_board.append(row)

    return new_board


def move_tiles(b):
    """Move tiles from right to left"""
    for x in range(4):
        for y in range(3):
            if sum(b[x][y:]):
                while b[x][y] == 0:
                    del b[x][y]
                    b[x].append(0)

            if sum(b[x][y + 1:]):
                while b[x][y + 1] == 0:
                    del b[x][y + 1]
                    b[x].append(0)

            if b[x][y] == b[x][y + 1]:
                b[x][y] *= 2
                b[x][y + 1] = 0

    return b


board = []

for i in range(4):
    board.append([int(x) for x in input().split()])

move = int(input())
board = prepare_board(move_tiles(prepare_board(board, move)), int((4 - move) % 4))

for i in board:
    print(*i)
