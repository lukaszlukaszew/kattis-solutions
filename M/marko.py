"""Marko"""

# marko

keyboard = {
    "0": "",
    "1": "",
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

word_count = int(input())
words = []

for i in range(word_count):
    words.append(input())

digits = input()

words = list(filter(lambda x: len(x) == len(digits), words))
check = {x: True for x in words}

for i, digit in enumerate(digits):
    for j in words:
        check[j] = check[j] and j[i] in keyboard[digit]

print(list(check.values()).count(True))
