"""Vaccine Efficacy"""

from sys import stdin
from collections import defaultdict

s = {}
for i in range(3):
    s[i] = defaultdict(int)

cases = int(stdin.readline())

for i in range(cases):
    line = stdin.readline()
    for j in range(3):
        s[j][line[0] + line[j + 1]] += 1

for i in range(3):
    res = 100 * (
        1
        - (
            s[i]["YY"]
            / (s[i]["YN"] + s[i]["YY"])
            / (s[i]["NY"] / (s[i]["NN"] + s[i]["NY"]))
        )
    )

    if res > 0:
        print(res)
    else:
        print("Not Effective")
