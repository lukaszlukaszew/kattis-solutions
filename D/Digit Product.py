"""Digit Product"""

num = input().replace("0", "")

while len(num) > 1:
    product = 1

    for i in num:
        product *= int(i)

    num = str(product).replace("0", "")

print(num)
