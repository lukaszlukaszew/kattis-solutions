"""From A to B"""

a, b = [int(x) for x in input().split()]
counter = 0

while a != b:
    if a > b:
        counter += 1
        if a % 2:
            a += 1
        else:
            a /= 2
    else:
        counter += b - a
        a = b

print(int(counter))
