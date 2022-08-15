"""Tracking Shares"""

# trackingshares

from collections import defaultdict

shares = defaultdict(dict)
days = set()

C = int(input())

for i in range(C):
    records = int(input())
    for j in range(records):
        amount, day = map(int, input().split())
        shares[i][day] = amount
        days.add(day)

days = sorted(days)
current = defaultdict(int)

for day in days:
    for i in range(C):
        current[i] = shares[i].get(day, current[i])
    print(sum(current.values()), end=" ")
