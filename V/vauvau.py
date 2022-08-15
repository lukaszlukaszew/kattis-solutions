"""Vauvau"""

# vauvau

A, B, C, D = [int(x) for x in input().split()]
heroes = [int(x) for x in input().split()]
results = {0: "none", 1: "one", 2: "both"}

for i in range(3):
    result = 0
    if 0 < heroes[i] % (A + B) <= A:
        result += 1
    if 0 < heroes[i] % (C + D) <= C:
        result += 1

    print(results[result])
