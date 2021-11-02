"""Disastrous Downtime"""

from collections import deque
from math import ceil

n, k = map(int, input().split())
ending = deque()
counter = 0
max_counter = 0

for i in range(n):
    start = int(input())
    ending.append(start + 1000)

    if start < ending[0]:
        counter += 1
        max_counter = max(counter, max_counter)
    else:
        while start >= ending[0]:
            ending.popleft()
            counter -= 1

        counter += 1
        max_counter = max(counter, max_counter)

print(int(ceil(max_counter / k)))
