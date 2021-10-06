"""Alien Numbers"""

test_cases = int(input())

for j in range(test_cases):
    an, sl, tl = input().split()
    stats = list()
    number_dec = 0

    for i in range(len(an)):
        number_dec += sl.index(an[i]) * (len(sl) ** (len(an) - i - 1))

    result = ""

    while number_dec > 0:
        result = tl[int(number_dec % len(tl))] + result
        number_dec = int(number_dec // len(tl))

    print("Case #" + str(j + 1) + ":", result)
