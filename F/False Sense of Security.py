"""False Sense of Security"""

Morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "_": "..--",
    ",": ".-.-",
    ".": "---.",
    "?": "----",
}

while True:
    try:
        line = input()
        morse_line, result, start, nums = "", "", 0, []

        for i in line:
            morse_line += Morse[i]
            nums.append(len(Morse[i]))

        for i, val in enumerate(reversed(nums)):
            result += tuple(Morse.keys())[
                tuple(Morse.values()).index(morse_line[start: start + val])
            ]
            start += val

        print(result)

    except EOFError:
        break
