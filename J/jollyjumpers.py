"""Jolly Jumpers"""

# jollyjumpers

from sys import exit, stdin

try:
    while True:
        n, *nums = map(int, stdin.readline().split())
        nums_set = {x + 1 for x in range(n - 1)}

        for i in range(n - 1):
            nums_set.discard(abs(nums[i + 1] - nums[i]))

        if nums_set:
            print("Not Jolly")
        else:
            print("Jolly")

except ValueError:
    exit()
