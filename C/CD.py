"""CD"""

from sys import stdin

while True:
    nums = [int(x) for x in stdin.readline().split()]

    if all(nums):
        cds = set()
        counter = 0

        for i in range(nums[0]):
            cds.add(stdin.readline())

        for i in range(nums[1]):
            if stdin.readline() in cds:
                counter += 1

        print(counter)
    else:
        break
