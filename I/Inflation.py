"""Inflation"""

# inflation

items = int(input())
canisters = sorted(list(map(int, input().split())))
result = []

for i in range(items):
    result.append(canisters[i] / (i + 1))

if max(result) > 1:
    print("impossible")
else:
    print(format(min(result), ".6f"))
