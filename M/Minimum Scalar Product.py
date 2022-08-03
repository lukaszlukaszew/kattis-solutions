"""Minimum Scalar Product"""

# minimumscalar

cases = int(input())

for i in range(cases):
    coordinates = int(input())
    result = 0

    X = sorted([int(x) for x in input().split()])
    Y = sorted([int(x) for x in input().split()], reverse=True)

    for x, val in enumerate(X):
        result += val * Y[x]

    print('Case #' + str(i+1) + ':', result)
