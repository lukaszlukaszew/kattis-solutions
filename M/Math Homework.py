"""Math Homework"""

birds, dogs, cats, legs = [int(x) for x in input().split()]
cases = []

for i in range(int(legs // birds) + 1):
    for j in range(int((legs - i * birds) // dogs) + 1):
        for k in range(int(((legs - i * birds) - j * dogs) // cats) + 1):
            if i * birds + j * dogs + k * cats == legs:
                cases.append((i, j, k))

if cases:
    for x in cases:
        print(*x)
else:
    print("impossible")
