"""Cinema Crowds 2"""

N, M = map(int, input().split())
nums = list(map(int, input().split()))

for i, val in enumerate(nums):
    if val <= N:
        N -= val
    else:
        break

print(len(nums[i:]))
