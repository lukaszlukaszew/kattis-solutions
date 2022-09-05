"""Sideways Sorting"""

# sidewayssorting

r, c = map(int, input().split())

while r + c:
    info, columns = [], []

    for i in range(r):
        line = input()
        for j in range(c):
            if i:
                info[j] += line[j]
            else:
                info.append(line[j])

    for i in info:
        columns.append((i.lower(), i))

    columns.sort()

    for i in range(r):
        result = []
        for j in columns:
            result.append(j[1][i])

        print("".join(result))

    print()

    r, c = map(int, input().split())
