"""Expected Earnings"""

n, k, p = map(float, input().split())

if n * p >= k:
    print("spela inte!")
else:
    print("spela")
