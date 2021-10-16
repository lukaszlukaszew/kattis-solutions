"""Saving For Retirement"""

B, Br, Bs, A, As = map(int, input().split())

bobs_cash = (Br - B) * Bs
alice = A
alices_cash = 0

while bobs_cash >= alices_cash:
    alice += 1
    alices_cash = (alice - A) * As

print(alice)
