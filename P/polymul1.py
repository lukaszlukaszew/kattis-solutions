"""Polynomial Multiplication 1"""

# polymul1

from sys import stdin

cases = int(input())

for i in range(cases):
    f_scale = int(input())
    line = (int(x) for x in stdin.readline().split())
    f = {f_scale - j: val for j, val in enumerate(line)}

    s_scale = int(input())
    line = (int(x) for x in stdin.readline().split())
    s = {s_scale - j: val for j, val in enumerate(line)}

    r_scale = f_scale + s_scale
    r = {r_scale - j: [0] for j in range(r_scale + 1)}

    for fk in f.keys():
        for sk in s.keys():
            r[fk + sk].append(f[fk] * s[sk])

    print(r_scale)

    for j in sorted(r.keys(), reverse=True):
        print(sum(r[j]), end=" ")
