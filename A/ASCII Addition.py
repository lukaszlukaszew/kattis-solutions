"""ASCII Addition"""

from ast import literal_eval

digits = {
    "0": "xxxxxx...xx...xx...xx...xx...xxxxxx",
    "1": "....x....x....x....x....x....x....x",
    "2": "xxxxx....x....xxxxxxx....x....xxxxx",
    "3": "xxxxx....x....xxxxxx....x....xxxxxx",
    "4": "x...xx...xx...xxxxxx....x....x....x",
    "5": "xxxxxx....x....xxxxx....x....xxxxxx",
    "6": "xxxxxx....x....xxxxxx...xx...xxxxxx",
    "7": "xxxxx....x....x....x....x....x....x",
    "8": "xxxxxx...xx...xxxxxxx...xx...xxxxxx",
    "9": "xxxxxx...xx...xxxxxx....x....xxxxxx",
    "+": ".......x....x..xxxxx..x....x.......",
}

inpt = []
result_int = ""
result = ""

for i in range(7):
    line = input()

    for j in range(0, len(line), 6):
        if i == 0:
            inpt.append(line[j: j + 5])
        else:
            inpt[int(j // 6)] += line[j: j + 5]

for i in inpt:
    for k, v in digits.items():
        if i == v:
            result_int += k

result_int = str(literal_eval(result_int))

for i in result_int:
    result += digits[i]

for i in range(7):
    line = ""

    for j in range(0, len(result_int)):
        line += result[5 * i + j * 35: 5 * i + 5 + j * 35] + "."

    print(line[:-1])
