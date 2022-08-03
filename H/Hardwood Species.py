"""Hardwood Species"""

# hardwoodspecies

from sys import stdin

trees = {}

for line in stdin:
    if line == "\n":
        break
    trees[line] = trees.get(line, 0) + 1

for k, v in sorted(trees.items()):
    print(k.rstrip(), v * 100 / sum(trees.values()))
