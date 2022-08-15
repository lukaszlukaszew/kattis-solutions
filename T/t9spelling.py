"""T9 Spelling"""

# t9spelling

keyboard = [
    " ",
    "",
    "abc",
    "def",
    "ghi",
    "jkl",
    "mno",
    "pqrs",
    "tuv",
    "wxyz",
]

cases = int(input())

for i in range(cases):
    text = input()
    result = ""

    for char in text:
        for key in keyboard:
            if char in key:
                result += " " * int(result.endswith(str(keyboard.index(key))))
                result += str(keyboard.index(key)) * (key.index(char) + 1)
    print(f"Case #{i+1}: {result}")
