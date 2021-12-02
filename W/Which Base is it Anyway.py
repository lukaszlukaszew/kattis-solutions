"""Which Base is it Anyway"""

cases = int(input())

for i in range(cases):
    case = input().split()

    octal, hexadecimal = 0, 0
    number = case[1][::-1]

    for j, val in enumerate(number):
        octal += int(val) * 8 ** j
        hexadecimal += int(val) * 16 ** j

    if "9" in number or "8" in number:
        octal *= 0

    print(int(case[0]), int(octal), int(case[1]), int(hexadecimal))
