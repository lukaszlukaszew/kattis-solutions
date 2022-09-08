"""Good Morning!"""

# goodmorning

from sys import stdin


def check(number):
    """Check if number is possible"""
    x = True
    for a, val in enumerate(number[:-1]):
        if number[a + 1] not in keyboard[val]:
            x = False

    return x


keyboard = {
    "0": "0",
    "1": "0123456789",
    "2": "2356890",
    "3": "369",
    "4": "4567890",
    "5": "89056",
    "6": "69",
    "7": "7890",
    "8": "890",
    "9": "9",
}

cases = int(stdin.readline())

for i in range(cases):
    num = int(stdin.readline())

    for j in range(num + 1):
        for k in (-1, 1):
            result = str(num + j * k)

            if check(result):
                print(result)
                break

        else:
            continue

        break
