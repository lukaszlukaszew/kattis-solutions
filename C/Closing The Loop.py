"""Closing The Loop"""

# closingtheloop

from collections import defaultdict

cases = int(input())

for i in range(cases):
    input()
    line = input().split()
    segments, result = defaultdict(list), 0

    for j in line:
        segments[j[-1]].append(int(j[:-1]))

    for k, v in segments.items():
        v.sort()

    while segments["B"] and segments["R"]:
        result += segments["B"].pop() + segments["R"].pop() - 2

    print(f'Case #{i+1}: {result}')
