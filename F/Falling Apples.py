"""Falling Apples"""

# apples

from sys import stdin, stdout

rows, columns = map(int, stdin.readline().split())
board = []
current = {}

for i in range(rows):
    board.append(list(stdin.readline().rstrip()))

for i in range(columns):
    current[i] = rows - 1

for i in range(rows - 1, -1, -1):
    for j in range(columns):
        if board[i][j] == "a":
            board[i][j] = "."
            board[current[j]][j] = "a"
            current[j] -= 1
        elif board[i][j] == "#":
            current[j] = i - 1

for i in range(rows):
    stdout.write("".join(board[i]) + "\n")
