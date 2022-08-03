"""ABC"""

# abc

nums = sorted(map(int, input().split()))
line = input()

print(" ".join([str(nums[ord(x) - ord("A")]) for x in line]))
