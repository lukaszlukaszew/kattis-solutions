"""DA-Sort"""

from sys import stdin
from collections import deque

cases = int(stdin.readline())

for i in range(cases):
    K, N = map(int, stdin.readline().split())
    nums = deque()

    while len(nums) < N:
        nums.extend(map(int, stdin.readline().split()))

    counter, border = 0, float("inf")

    while border >= min(nums):
        ind = nums.index(min(nums))
        counter += ind

        for j in range(ind):
            border = min(border, nums.popleft())

        nums.popleft()

        if not nums:
            break

    counter += len(nums)
    print(K, counter)
