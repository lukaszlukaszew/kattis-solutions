"""Hiding Places"""

# hidingplaces

from collections import defaultdict, deque

jumps = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, -2), (-1, 2))
columns = "abcdefgh"

cases = int(input())

for i in range(cases):
    summary, moves, visited = defaultdict(list), deque(), set()

    start_tile = input()
    start = (8 - int(start_tile[1]), columns.index(start_tile[0]))
    visited.add(start)
    moves.append((start, 0))

    while moves:
        (y, x), dist = moves.popleft()
        summary[dist].append((y, x))

        for j in jumps:
            if 0 <= y + j[0] < 8 and 0 <= x + j[1] < 8 and (y + j[0], x + j[1]) not in visited:
                moves.append(((y + j[0], x + j[1]), dist + 1))
                visited.add((y + j[0], x + j[1]))

    result = list(map(lambda a: columns[a[1]] + str(8 - a[0]), sorted(summary[max(summary.keys())])))

    print(str(max(summary.keys())), " ".join(result), sep=" ")
