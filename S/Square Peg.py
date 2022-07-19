"""Square Peg"""

# squarepeg

L, R = map(int, input().split())

if 2 * R >= L * 2 ** .5:
    print("fits")
else:
    print("nope")
