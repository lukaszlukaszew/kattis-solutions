"""Islands"""

# islands3

r, c = [int(x) for x in input().split()]
picture, islands = [], 0


def change(x, y, pic):
    """Process picture"""
    pic[y][x] = "W"

    for m in (-1, 0, 1):
        for n in (-1, 0, 1):
            if 0 <= x + m < c and 0 <= y + n < r and abs(m) != abs(n):
                if pic[y + n][x + m] in "LC":
                    change(x + m, y + n, pic)


for i in range(r):
    picture.append(list(input()))

for i in range(r):
    for j in range(c):
        if picture[i][j] == "L":
            islands += 1
            change(j, i, picture)

print(islands)
