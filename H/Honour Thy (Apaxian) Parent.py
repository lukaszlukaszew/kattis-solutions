"""Honour Thy (Apaxian) Parent"""

Y, P = input().split()

if Y[-2:] == "ex":
    print(Y + P)
elif Y[-1] in "aioue":
    print(Y[:-1] + "ex" + P)
else:
    print(Y + "ex" + P)
