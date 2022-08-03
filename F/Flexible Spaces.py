"""Flexible Spaces"""

# flexible

from itertools import combinations

W, P = map(int, input().split())
spaces = [*list(map(int, input().split())), 0, W]
result = set()
for i in combinations(spaces, 2):
    result.add(abs(i[0] - i[1]))

result.discard(0)
print(*sorted(set(result)))
