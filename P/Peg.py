"""Peg"""

# peg

rows, counter = [], 0

for i in range(7):
    rows.append(input())

for i in range(7):
    column = ""
    for j in range(7):
        column += rows[j][i]
    rows.append(column)

for i in rows:
    for j in ("oo.", ".oo"):
        counter += i.count(j)

print(counter)
