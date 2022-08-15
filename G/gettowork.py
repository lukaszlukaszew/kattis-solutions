"""Get to Work"""

# gettowork

from collections import defaultdict

cases = int(input())

for i in range(cases):
    N, T = [int(x) for x in input().split()]
    N = list(range(1, N + 1))

    employees, capacities = defaultdict(int), defaultdict(list)
    cars, empl = defaultdict(int), int(input())

    for j in range(empl):
        town, capacity = [int(x) for x in input().split()]
        employees[town] += 1
        capacities[town].append(capacity)

    for k in N:
        if k == T:
            employees[k] = 0
            continue

        for j in sorted(capacities[k], reverse=True):
            if employees[k] <= 0:
                break

            employees[k] -= min(j, employees[k])
            cars[k] += 1

    result = "Case #" + str(i + 1) + ":"

    if sum(employees.values()):
        caps = ["IMPOSSIBLE"]
    else:
        caps = [cars[x] for x in N]

    print(result, *caps)
