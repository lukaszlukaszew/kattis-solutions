"""Peragrams"""

from collections import Counter

line = Counter(input())
print(max(0, len(list(filter(lambda x: x % 2, line.values()))) - 1))
