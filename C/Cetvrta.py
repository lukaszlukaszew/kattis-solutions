"""Cetvrta"""

x = []
y = []

for i in range(3):
    X, Y = input().split()
    x.append(X)
    y.append(Y)

for i in range(3):
    if x.count(x[i]) == 1:
        X = x[i]
    if y.count(y[i]) == 1:
        Y = y[i]

print(X, Y)
