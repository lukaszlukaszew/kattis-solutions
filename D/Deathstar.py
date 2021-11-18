"""Deathstar"""

N = int(input())
container = {}

for i in range(N):
    line = [int(x) for x in input().split()]
    for j in range(N):
        if i != j:
            container[i] = container.get(i, line[j]) | line[j]
            container[j] = container.get(j, line[j]) | line[j]

print(*[container[x] for x in sorted(container.keys())])
