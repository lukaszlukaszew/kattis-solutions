"""Emag Eht Htiw Em Pleh"""

# empleh

from string import ascii_lowercase

board = []
border = ["+"] + (["-"] * 3 + ["+"]) * 8

for i in range(17):
    if not i % 2:
        board.append(border)
    else:
        board.append(
            ["|"]
            + (["."] * 3 + ["|"] + [":"] * 3 + ["|"]) * 4 * int(1 - ((i // 2) % 2))
            + ([":"] * 3 + ["|"] + ["."] * 3 + ["|"]) * 4 * int((i // 2) % 2)
        )

figures = [("P" + x)[-3:] for x in input().replace("White: ", "").split(",")]
figures.extend([("p" + x.lower())[-3:] for x in input().replace("Black: ", "").split(",")])

while figures:
    try:
        figure, column, row = list(figures.pop())
        board[17 - 2 * int(row)][ascii_lowercase.index(column) * 4 + 2] = figure
    except ValueError:
        continue

for i in board:
    print("".join(i))
