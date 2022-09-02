"""Falcon Dive"""

# falcondive

from sys import stdin

frame1, frame2 = [], []
falcon1, falcon2 = [], []

rows, columns, falc = stdin.readline().split()
rows, columns, falc = int(rows), int(columns), falc[1:-1]

for i in range(rows):
    frame1.append(list(stdin.readline().rstrip()))

input()

for i in range(rows):
    frame2.append(list(stdin.readline().rstrip()))

for r in range(rows):
    for c in range(columns):
        if frame1[r][c] == falc:
            falcon1.append((r, c))
            frame1[r][c] = frame2[r][c]
        elif frame2[r][c] == falc:
            falcon2.append((r, c))

falcon1.sort()
falcon2.sort()

delta_y, delta_x = falcon2[0][0] - falcon1[0][0], falcon2[0][1] - falcon1[0][1]

for y, x in falcon2:
    if 0 <= delta_y + y < rows and 0 <= delta_x + x < columns:
        frame1[delta_y + y][delta_x + x] = falc

for i in range(rows):
    print("".join(frame1[i]))
