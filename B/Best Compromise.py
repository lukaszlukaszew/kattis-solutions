"""Best Compromise"""

from collections import defaultdict

scenarios = int(input())

for i in range(scenarios):
    n, m = [int(x) for x in input().split()]
    opinions = defaultdict(int)

    for j in range(n):
        opinion = input()
        for k in range(m):
            opinions[k] += int(opinion[k])

    result = ""
    for j in range(m):
        result += str(int(opinions[j] > n / 2))

    print(result)
