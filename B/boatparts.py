"""Boat Parts"""

# boatparts

parts, days = map(int, input().split())
replaced = set()
counter = 0

for i in range(days):
    replaced.add(input())
    if len(replaced) < parts:
        counter += 1

if len(replaced) == parts:
    print(counter + 1)
else:
    print("paradox avoided")
