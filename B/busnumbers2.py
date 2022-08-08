"""Bus Numbers"""

# busnumbers2

from itertools import combinations
from collections import Counter

n = int(input())
nums = []

for i in range(1, n):
    if i ** 3 >= n:
        break

    nums.append(i**3)

all_sums = Counter(list(map(lambda x: x * 2, nums)) + list(map(sum, combinations(nums, 2))))
possibles = list((filter(lambda x: all_sums[x] >= 2 and x <= n, all_sums)))

if possibles:
    print(max(possibles))
else:
    print("none")
