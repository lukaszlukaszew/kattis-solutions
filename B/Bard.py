"""Bard"""

villagers = int(input())
evenings = int(input())
known = set()

for i in range(evenings):
    per_evening = input().split()
    villagers_per_evening = set(per_evening[1:])

    if "1" in villagers_per_evening:
        known = known.intersection(villagers_per_evening)
    else:
        known = known.union(villagers_per_evening)

known = sorted(list(map(int, known)))

if 1 not in known:
    print(1)

for i in known:
    print(i)
