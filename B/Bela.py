"""Bela"""

D = {"A": 11, "K": 4, "Q": 3, "J": 20, "T": 10, "9": 14, "8": 0, "7": 0}
ND = {"A": 11, "K": 4, "Q": 3, "J": 2, "T": 10, "9": 0, "8": 0, "7": 0}

N, B = input().split()
result = 0

for i in range(int(N) * 4):
    line = input()
    if line[1] == B:
        result += D[line[0]]
    else:
        result += ND[line[0]]

print(result)
