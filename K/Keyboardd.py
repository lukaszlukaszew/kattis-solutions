"""Keyboardd"""

from collections import Counter
from sys import stdin

line = Counter(stdin.readline())
line2 = Counter(stdin.readline())

result = ""

for k, v in line.items():
    if v != line2[k]:
        result += k

print(result)
