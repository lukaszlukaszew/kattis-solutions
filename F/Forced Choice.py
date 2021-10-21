"""Forced Choice"""

from sys import stdin

N, P, S = map(int, stdin.readline().split())

for i in range(S):
    line = list(map(int, stdin.readline().split()))[1:]

    if P in line:
        print("KEEP")
    else:
        print("REMOVE")
