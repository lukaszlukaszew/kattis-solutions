x = 1

while x < 99:
    print(x)
    x = int(input())
    x += min(3 - (x % 3), 2)

print(99)
