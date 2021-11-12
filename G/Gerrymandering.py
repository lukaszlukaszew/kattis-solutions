"""Gerrymandering"""

P, D = [int(x) for x in input().split()]
distr_A, distr_B = {}, {}
tot_wast_A, tot_wast_B, total = 0, 0, 0

for i in range(P):
    district, A, B = [int(x) for x in input().split()]
    distr_A[district] = distr_A.get(district, 0) + A
    distr_B[district] = distr_B.get(district, 0) + B

for i in sorted(distr_A.keys()):
    if distr_A[i] > distr_B[i]:
        wast_A = distr_A[i] - (int((distr_A[i] + distr_B[i]) // 2) + 1)
        wast_B = distr_B[i]
        print("A", wast_A, wast_B)
    else:
        wast_A = distr_A[i]
        wast_B = distr_B[i] - (int((distr_A[i] + distr_B[i]) // 2) + 1)
        print("B", wast_A, wast_B)

    tot_wast_A += wast_A
    tot_wast_B += wast_B
    total += distr_A[i] + distr_B[i]

print(abs(tot_wast_A - tot_wast_B) / total)
