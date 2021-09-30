from collections import defaultdict

N, K = [int(x) for x in input().split()]

nums = defaultdict(bool)
nums.default_factory = lambda: True

i = 2

while K > 0:
    for j in range(i, N+1, i):
        if nums[j]:
            nums[j] = False
            K -= 1
            if not K:
                print(j)
                break

    i += 1
