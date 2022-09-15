"""George"""

# george

from sys import stdin
from collections import defaultdict

N, M = [int(x) for x in stdin.readline().split()]
A, B, K, G = [int(x) for x in stdin.readline().split()]

route = [int(x) for x in stdin.readline().split()]
graph, costs, parents, processed = defaultdict(dict), {}, {}, set()
path, time = {}, -K
processed.add(A)

for i in range(M):
    start, end, cost = [int(x) for x in stdin.readline().split()]
    graph[start][end], graph[end][start] = cost, cost

first = set(graph[A].keys())

for i in range(1, N + 1):
    if i == A:
        costs[i] = 0
    elif i in first:
        parents[i] = A
        costs[i] = graph[A][i]
    else:
        costs[i] = float("inf")

for i in range(G - 1):
    path[(route[i], route[i + 1])] = time
    path[(route[i + 1], route[i])] = time
    time += graph[route[i]][route[i + 1]]


def smallest_cost():
    """Find node with lowest cost which wasn't processed yet"""
    lowest_cost, lowest = float("inf"), None

    for k, v in costs.items():
        if k in processed:
            continue
        if lowest_cost > v:
            lowest_cost = v
            lowest = k

    return lowest


next_one = smallest_cost()

while next_one is not None:
    neighbors = list(graph[next_one].keys())

    for neighbor, cost in graph[next_one].items():
        for key, value in path.items():
            if key == (next_one, neighbor) and value <= costs[next_one] <= value + cost:
                costs[neighbor] = value + 2 * cost
                parents[neighbor] = next_one
                break

        else:
            difference = costs[next_one] + cost

            if difference < costs[neighbor]:
                costs[neighbor] = difference
                parents[neighbor] = next_one

    processed.add(next_one)
    next_one = smallest_cost()

print(costs[B])
