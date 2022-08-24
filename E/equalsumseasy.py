"""Equal Sums (Easy)"""

# equalsumseasy

from itertools import combinations
from collections import defaultdict

test_cases = int(input())

for i in range(test_cases):
    numbers = [int(x) for x in input().split()][1:]
    print(f"Case #{i + 1}:")
    possibilities = defaultdict(set)

    for j in range(len(numbers)):
        for comb in combinations(numbers, j):
            possibilities[sum(comb)].add(tuple(sorted(comb)))
            if len(possibilities[sum(comb)]) == 2:
                for k in possibilities[sum(comb)]:
                    print(*k)
                break

        else:
            continue

        break

    else:
        print("Impossible")
