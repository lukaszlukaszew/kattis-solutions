"""This Ain't Your Grandpa's Checkerboard"""

# thisaintyourgrandpascheckerboard

dimension = int(input())

board = {"rows": [], "columns": []}
result = 1

for i in range(dimension):
    board["rows"].append(input())

for i in range(dimension):
    column = ""
    for j in range(dimension):
        column += board["rows"][j][i]
    board["columns"].append(column)

for k, v in board.items():
    for i in v:
        if any(["BBB" in i, "WWW" in i, i.count("W") != i.count("B")]):
            result -= 1

print(min(max(result, 0), 1))
