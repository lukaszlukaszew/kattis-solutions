"""No Duplicates"""

from collections import Counter

line = input().split()
counter = Counter(line)

if max(counter.values()) > 1:
    print("no")
else:
    print("yes")
