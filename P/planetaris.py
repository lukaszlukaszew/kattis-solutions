"""Planetaris"""

# planetaris

n, ships = [int(x) for x in input().split()]
systems = [int(x) + 1 for x in input().split()]

systems.sort()
possible = 0

if ships >= sum(systems):
    print(n)
else:
    for i in range(n):
        if possible + systems[i] <= ships:
            possible += systems[i]
        else:
            break

    print(i)
