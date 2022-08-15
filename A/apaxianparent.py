"""Honour Thy (Apaxian) Parent"""

# apaxianparent

Y, P = input().split()

if Y[-2:] == "ex":
    print(Y + P)
elif Y[-1] in "aioue":
    print(Y[:-1] + "ex" + P)
else:
    print(Y + "ex" + P)
