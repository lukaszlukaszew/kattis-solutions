"""YODA"""

# yoda

N = list(input())
M = list(input())

for i in range(-1, -min(len(M), len(N)) - 1, -1):
    if N[i] > M[i]:
        M[i] = ""
    elif N[i] < M[i]:
        N[i] = ""

N = "".join(N)
M = "".join(M)

if N and M:
    print(int(N))
    print(int(M))
else:
    if N:
        print(N)
        print("YODA")
    else:
        print("YODA")
        print(M)
