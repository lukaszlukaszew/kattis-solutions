"""Wizard of Odds"""

N, K = [int(x) for x in input().split()]
N = N / (2 ** K)

if N <= 1:
    print("Your wish is granted!")
else:
    print("You will become a flying monkey!")
