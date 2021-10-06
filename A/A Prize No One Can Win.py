"""A Prize No One Can Win"""

n, X = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

maximum = 0
counter = 0

nums.sort()

if len(nums) > 1:
    for i in nums:
        if maximum + i <= X:
            counter += 1
            maximum = max(maximum, i)
        else:
            break
    if not counter:
        counter += 1
else:
    counter += 1

print(counter)
