"""Sum Squared Digits Function"""

# sumsquareddigits

cases = int(input())

for i in range(cases):
    case, base, number = [int(x) for x in input().split()]
    exponents, j, result = [], 0, 0
    exponent = base ** j

    while exponent <= number:
        exponents.append(exponent)
        j += 1
        exponent = base ** j

    exponents.sort(reverse=True)

    for j in exponents:
        result += int((number // j) ** 2)
        number = int(number % j)

    print(case, result)
