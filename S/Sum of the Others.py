"""Sum of the Others"""

# sumoftheothers

while True:
    try:
        nums = list(map(int, input().split()))
        summary = sum(nums)
        for i, val in enumerate(nums):
            if summary - val == val:
                print(val)
                break
    except EOFError:
        break
