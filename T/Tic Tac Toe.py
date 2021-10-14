"""Tic Tac Toe"""

cases = int(input())
winning = (
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 4, 8),
    (2, 4, 6),
)

for i in range(cases):
    board, x, o, possible = "", 0, 0, 1
    for j in range(3):
        line = input()
        x += line.count("X")
        o += line.count("O")
        board += line

    if i != cases - 1:
        input()

    if x == o:
        for j in winning:
            if board[j[0]] == board[j[1]] == board[j[2]] == "X":
                possible = 0
    elif x == o + 1:
        for j in winning:
            if board[j[0]] == board[j[1]] == board[j[2]] == "O":
                possible = 0
    else:
        possible = 0

    if possible:
        print("yes")
    else:
        print("no")
