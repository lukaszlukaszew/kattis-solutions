"""Overdraft"""

# overdraft

result, current, transactions = 0, 0, int(input())

for i in range(transactions):
    current += int(input())
    result = min(current, result)

print(-result)
