"""Graduation"""

# skolavslutningen

N, M, K = [int(x) for x in input().split()]
columns, colors = [], set()

for i in range(M):
    columns.append(set())

for i in range(N):
    line = input()
    for j in range(M):
        columns[j].add(line[j])

while columns:
    for j in range(1, len(columns)):
        if columns[0].intersection(columns[j]):
            columns[0] = columns[0] | columns[j]
            columns.remove(columns[j])
            break
    else:
        colors.add(tuple(columns[0]))
        columns.pop(0)

print(len(colors))
