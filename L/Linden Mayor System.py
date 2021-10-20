"""Linden Mayor System"""

n, m = [int(x) for x in input().split()]
changes = {}

for i in range(n):
    x, changes[x] = list(input().split(" -> "))

string = list(input())

for i in range(m):
    result = []

    for j in string:
        result.extend(changes.get(j, j))

    string = result

print("".join(string))
