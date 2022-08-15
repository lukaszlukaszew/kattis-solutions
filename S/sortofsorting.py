"""Sort of Sorting"""

# sortofsorting

from collections import defaultdict

names_count = int(input())

while names_count:
    names = defaultdict(list)

    for i in range(names_count):
        line = input()
        names[line[:2]].append(line)

    for i in sorted(names.keys()):
        for j in names[i]:
            print(j)

    print()

    names_count = int(input())
