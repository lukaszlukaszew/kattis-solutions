"""Conformity"""

from collections import defaultdict
from sys import stdin

frosh_num = int(input())
combinations = defaultdict(int)

for i in range(frosh_num):
    combinations[tuple(sorted(map(int, stdin.readline().split())))] += 1

print(
    max(combinations.values())
    * list(combinations.values()).count(max(combinations.values()))
)
