"""Okvir"""

# okvir

M, N = [int(x) for x in input().split()]
U, L, R, D = [int(x) for x in input().split()]

words, lines = [], []

for i in range(M):
    words.append(input())

for i in range(U + D + M):
    line = ""
    for j in range(L + R + N):
        if (i + j) % 2:
            line += "."
        else:
            line += "#"

    lines.append(line)

for i in range(M):
    lines[U + i] = lines[U + i][:L] + words[i] + lines[U + i][L + N:]

for line in lines:
    print(line)
