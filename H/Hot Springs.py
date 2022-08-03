"""Hot Springs"""

# hotsprings

from sys import stdin

nums = int(stdin.readline())
num = sorted(map(int, stdin.readline().split()))

left = num[: int(nums / 2)]
right = sorted(num[int(nums / 2):], reverse=True)
result = []

while left and right:
    result.append(right.pop())
    result.append(left.pop())

print(*result, *left, *right)
