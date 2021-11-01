"""Oddities"""

nums = int(input())

for i in range(nums):
    num = int(input())
    if num % 2:
        print(f"{num} is odd")
    else:
        print(f"{num} is even")
