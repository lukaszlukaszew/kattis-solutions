"""Espresso Bucks"""

# espressobucks

land = []
row, column = map(int, input().split())

for i in range(row):
    land.append(list(input()))

for i in range(row):
    for j in range(column):
        if land[i][j] == ".":
            if (
                (i == 0 and j == 0)
                or (i == 0 and land[i][j - 1] != "E")
                or (j == 0 and land[i - 1][j] != "E")
                or (land[i - 1][j] != "E" and land[i][j - 1] != "E")
            ):
                land[i][j] = "E"
for k in land:
    print("".join(k))
