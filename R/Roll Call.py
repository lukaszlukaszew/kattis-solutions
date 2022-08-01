"""Roll Call"""

# rollcall

from collections import defaultdict, Counter

people = defaultdict(list)
names = []

try:
    while True:
        first_name, last_name = input().split()
        people[last_name].append(first_name)
        names.append(first_name)

except EOFError:
    names = Counter(names)
    for k in sorted(people.keys()):
        for v in sorted(people[k]):
            print(v, k * int(names[v] > 1))
