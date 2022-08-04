"""Warehouse"""

# warehouse

from collections import defaultdict

cases = int(input())

for i in range(cases):
    entries = int(input())
    entities = defaultdict(int)

    for j in range(entries):
        line = input().split()
        entities[line[0]] += int(line[1])

    sorted_entities = defaultdict(list)

    for k, v in entities.items():
        sorted_entities[v].append(k)

    print(len(entities))
    for j in sorted(sorted_entities.keys(), reverse=True):
        for k in sorted(sorted_entities[j]):
            print(k, j)
