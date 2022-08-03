"""I Wanna Be The Very Best"""

# iwannabe

pokes, K = [int(x) for x in input().split()]
stats = {0: {}, 1: {}, 2: {}}

for i in range(pokes):
    line = [int(x) for x in input().split()]
    for j, val in enumerate(line):
        stats[j][val] = i

result = set()

for i in range(3):
    for j, key in enumerate(sorted(stats[i].keys(), reverse=True)):
        if j < K:
            result.add(stats[i][key])
        else:
            break

print(len(result))
