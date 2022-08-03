"""Babylonian Numbers"""

# babylonian

numbers = int(input())

for i in range(numbers):
    number = input().replace(",", ",0")
    max_power = number.count(",")
    number_decimal = 0

    for j in range(max_power):
        number_decimal += int(number[: number.index(",")]) * (60 ** (max_power - j))
        number = number[number.index(",") + 1:]

    number_decimal += int(number)

    print(number_decimal)
