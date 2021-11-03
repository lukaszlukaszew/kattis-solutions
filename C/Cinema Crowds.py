"""Cinema Crowds"""

from collections import deque

N, M = map(int, input().split())
nums = deque(map(int, input().split()))
counter = 0

while nums:
    group = nums.popleft()
    if N >= group:
        N -= group
    else:
        counter += 1

print(counter)
