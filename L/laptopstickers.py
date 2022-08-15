"""Laptop Stickers"""

# laptopstickers

from string import ascii_lowercase

C, R, K = map(int, input().split())
laptop = [["_" for _ in range(C)] for _ in range(R)]
stickers = ascii_lowercase

for i in range(K):
    l, h, x, y = map(int, input().split())

    for j in range(l):
        for k in range(h):
            if x + j < C and y + k < R:
                laptop[y+k][x+j] = stickers[i]

for row in laptop:
    print("".join(row))
