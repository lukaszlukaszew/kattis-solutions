"""A Towering Problem"""

# towering

from itertools import combinations

*boxes, h1, h2 = map(int, input().split())
groups, group1, group2 = [], [], []

for i in combinations(boxes, 3):
    if sum(i) == h1 and not group1:
        group1 = i
    elif sum(i) == h2 and not group2:
        group2 = i
    elif group1 and group2:
        break

print(*sorted(group1, reverse=True), *sorted(group2, reverse=True))
