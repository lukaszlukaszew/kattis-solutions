"""Basic Programming 2"""

# basicprogramming2

from collections import Counter

num, action = map(int, input().split())
nums = list(map(int, input().split()))

if action == 1:
    nums = set(nums)
    for i in nums:
        if 7777 - i in nums:
            print("Yes")
            break
    else:
        print("No")
elif action == 2:
    if len(set(nums)) == len(nums):
        print("Unique")
    else:
        print("Contains duplicate")
elif action == 3:
    nums = Counter(nums)
    for k, v in nums.items():
        if v > num / 2:
            print(k)
            break
    else:
        print(-1)
elif action == 4:
    nums.sort()
    if num % 2:
        print(nums[int(num / 2)])
    else:
        print(nums[int(num / 2) - 1], nums[int(num / 2)])
elif action == 5:
    print(*sorted(list(filter(lambda x: 100 <= x <= 999, nums))))
