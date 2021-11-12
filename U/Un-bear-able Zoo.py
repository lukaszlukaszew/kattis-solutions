"""Un-bear-able Zoo"""

from collections import defaultdict

counter = 1
animals = int(input())

while animals:
    zoo = defaultdict(int)

    for i in range(animals):
        zoo[input().lower().split()[-1]] += 1

    print(f"List {counter}:")
    for k, v in sorted(zoo.items()):
        print(k, "|", v)

    animals = int(input())
    counter += 1
