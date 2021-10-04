"""Watch Out For Those Hailstones!"""


def func(num):
    result = None
    if num == 1:
        result = 1
    elif num % 2:
        result = num + func(3 * num + 1)
    else:
        result = num + func(num // 2)

    return result


print(int(func(int(input()))))
