"""Odd Man Out"""

# oddmanout

from collections import Counter

cases = int(input())

for i in range(cases):
    input()
    guests = Counter(input().split())
    print(f"Case #{i+1}: {list(guests.keys())[list(guests.values()).index(1)]}")
