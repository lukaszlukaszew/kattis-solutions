"""Incognito"""

from collections import defaultdict

cases = int(input())

for i in range(cases):
    clothes = defaultdict(list)
    different = int(input())

    for j in range(different):
        name, category = input().split()
        clothes[category].append(name)

    counter = 1
    for v in clothes.values():
        counter *= len(v) + 1

    print(counter - 1)
