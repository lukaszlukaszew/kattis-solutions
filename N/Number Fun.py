"""Number Fun"""

# numberfun

cases = int(input())

for i in range(cases):
    a, b, c = map(int, input().split())

    if c in [a + b, a * b, abs(a - b), a / b, b / a]:
        print("Possible")
    else:
        print("Impossible")
