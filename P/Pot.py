"""Pot"""

cases = int(input())
result = 0

for i in range(cases):
    num = input()
    result += int(num[:-1]) ** int(num[-1])

print(result)
