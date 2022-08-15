"""Prva"""

# prva

R, C = [int(x) for x in input().split()]
rows, columns, words = [], [], []

for i in range(R):
    rows.append(input())

for i in range(C):
    column = ""
    for j in rows:
        column += j[i]
    columns[i] = column

for i in rows:
    for j in i.split("#"):
        words.append(j)

for i in columns:
    for j in i.split("#"):
        words.append(j)

words.sort()

for i in words:
    if len(i) >= 2:
        print(i)
        break
