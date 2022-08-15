"""One Chicken Per Person!"""

# onechicken

N, M = map(int, input().split())

num = M - N
unit = "piece" + "s" * int(abs(num) != 1)

if num >= 0:
    print(f"Dr. Chaz will have {num} {unit} of chicken left over!")
else:
    print(f"Dr. Chaz needs {abs(num)} more {unit} of chicken!")
