"""Harshad Numbers"""

num = int(input())

while True:
    if num % sum(map(int, list(str(num)))):
        num = int(num) + 1
    else:
        print(num)
        break
