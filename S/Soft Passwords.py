"""Soft Password"""

S, P = input(), input()

result = [
    S == P,
    S == P.swapcase(),
    P in S and ((S[0].isnumeric() or S[-1].isnumeric()) and len(S) == len(P) + 1),
]

if any(result):
    print("Yes")
else:
    print("No")
