"""Mosquito Multiplication"""

import sys

try:
    while True:
        M, P, L, E, R, S, N = map(int, input().split())

        for i in range(N):
            eggs = M * E
            M = int(P // S)
            P = int(L // R)
            L = eggs

        print(M)

except EOFError:
    sys.exit()
