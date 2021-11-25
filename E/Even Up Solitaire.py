"""Even Up Solitaire"""

from sys import stdin

num_count = int(stdin.readline())
nums = [int(x) % 2 for x in stdin.readline().split()]
stack = nums[:1]

for i in nums[1:]:
    if stack:
        if i == stack[-1]:
            stack.pop()
            continue

    stack.append(i)

print(len(stack))
