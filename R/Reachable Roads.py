"""Reachable Roads"""

# reachableroads

from collections import defaultdict

n = int(input())

for i in range(n):
    m, r = int(input()), int(input())
    cities, roads, result = {int(x) for x in range(m)}, defaultdict(list), -1

    for j in range(r):
        x, y = map(int, input().split())
        roads[x].append(y)
        roads[y].append(x)

    while cities:
        result += 1
        queue, visited = [], set()
        queue.append(cities.pop())

        while queue:
            start = queue.pop()
            visited.add(start)

            for j in roads[start]:
                if j not in visited:
                    queue.append(j)

        cities = cities.difference(visited)

    print(result)
