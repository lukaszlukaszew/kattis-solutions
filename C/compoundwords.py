"""Compound Words"""

# compoundwords

from sys import stdin
from itertools import permutations

words, another_words = set(), set()
line = set(stdin.readline().split())

while line:
    words = words.union(line)
    line = set(stdin.readline().split())

for i in permutations(words, 2):
    another_words.add(i[0] + i[1])

another_words = sorted(another_words)

for j in another_words:
    print(j)
