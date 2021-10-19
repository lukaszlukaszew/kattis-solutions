"""Some Sum"""

num = int(input())

if num % 2:
    print("Either")
else:
    if (num / 2) % 2:
        print("Odd")
    else:
        print("Even")
