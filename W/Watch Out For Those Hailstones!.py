def func(num):
    if num == 1:
        return 1
    elif num % 2:
        return num + func(3*num + 1)
    else:
        return num + func(num//2)

print(int(func(int(input()))))
