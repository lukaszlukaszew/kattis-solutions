"""Secret Chamber at Mount Rushmore"""

# secretchamber

from collections import defaultdict

possibles, li = defaultdict(set), defaultdict(set)
m, n = [int(x) for x in input().split()]

for i in range(m):
    line = input().split()
    li[line[0]] = li[line[0]] | set(line[1])

for k, v in li.items():
    res_len = -1

    while res_len != len(v):
        res_len, temp = len(v), set()

        for j in v:
            temp = temp | li.get(j, set())

        v = temp | v

    possibles[k] = v

for i in range(n):
    line = input().split()

    if len(line[0]) != len(line[1]):
        print("no")
        continue

    result = "yes"
    for j in range(len(line[0])):
        if line[1][j] not in possibles.get(line[0][j], set()) and line[1][j] != line[0][j]:
            result = "no"

    print(result)
