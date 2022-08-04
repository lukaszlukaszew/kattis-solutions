"""Time Traveling Temperatures"""

# temperature

X, Y = [int(x) for x in input().split()]

if Y == 1 and not X:
    print("ALL GOOD")
elif Y == 1:
    print("IMPOSSIBLE")
else:
    print(X / (1 - Y))
