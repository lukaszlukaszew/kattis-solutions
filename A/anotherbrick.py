"""Another Brick in the Wall"""

# anotherbrick

h, w, n = map(int, input().split())
x = list(map(int, input().split()))[::-1]

for i in range(h):
    row = 0

    while row < w and x:
        row += x[-1]
        x.pop()

    if row != w:
        break

if i == h - 1 and row == w:
    print("YES")
else:
    print("NO")
