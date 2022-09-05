"""Rečenice"""

# recenice

from re import sub

digits = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

elev = {
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
}

tens = {
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety",
}

hundreds = {
    "1": "onehundred",
    "2": "twohundred",
    "3": "threehundred",
    "4": "fourhundred",
    "5": "fivehundred",
    "6": "sixhundred",
    "7": "sevenhundred",
    "8": "eighthundred",
    "9": "ninehundred",
}


words = int(input())
lenght, number, sentence = 0, "", []

for i in range(words):
    sentence.append(input())
    lenght += len(sentence[-1])

sentence = " ".join(sentence)

for i in range(10):
    for j in range(10):
        for k in range(10):
            if i + j + k:
                num = int(str(i) + str(j) + str(k))

                number = hundreds.get(str(i), "") + elev.get(
                    str(j) + str(k), tens.get(str(j), "") + digits.get(str(k), "")
                )

                if num == lenght - 1 + len(number):
                    break
        else:
            continue

        break

    else:
        continue

    break

print(sub("\$", number, sentence))
