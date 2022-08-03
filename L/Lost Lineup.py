"""Lost Lineup"""

# lostlineup

people = int(input())
nums = list(map(int, input().split()))
line = ["1" for x in range(people)]

for i in range(people - 1):
    line[nums[i] + 1] = str(i + 2)

print(" ".join(line))
