"""Basic Programming 1"""

# basicprogramming1

from string import ascii_lowercase

num, action = map(int, input().split())
nums = list(map(int, input().split()))

if action == 1:
    print(7)
elif action == 2:
    if nums[0] > nums[1]:
        print("Bigger")
    elif nums[0] == nums[1]:
        print("Equal")
    else:
        print("Smaller")
elif action == 3:
    print(sum(nums[:3]) - max(nums[:3]) - min(nums[:3]))
elif action == 4:
    print(sum(nums))
elif action == 5:
    print(sum(filter(lambda x: x % 2 == 0, nums)))
elif action == 6:
    print("".join(map(lambda x: ascii_lowercase[int(x % 26)], nums)))
elif action == 7:
    indices = set()
    result = ["Done", "Cyclic", "Out"]
    ind = 0
    while True:
        indices.add(ind)
        ind = nums[ind]
        check = [ind == num - 1, ind in indices, ind < 0 or ind >= num]
        if any(check):
            break

    print("".join(map(lambda x, y: x * int(y), result, check)))
