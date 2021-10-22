"""Flipping Patties"""

orders = int(input())
actions = {}

for i in range(orders):
    flip, pick = [int(x) for x in input().split()]
    for j in range(3):
        actions[pick - flip * j] = actions.get(pick - flip * j, 0) + 1

print(int(max(actions.values()) // 2 + max(actions.values()) % 2))
