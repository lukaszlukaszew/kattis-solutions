"""Soundex"""

letters = {
    "B": "1",
    "F": "1",
    "P": "1",
    "V": "1",
    "C": "2",
    "G": "2",
    "J": "2",
    "K": "2",
    "Q": "2",
    "S": "2",
    "X": "2",
    "Z": "2",
    "D": "3",
    "T": "3",
    "L": "4",
    "M": "5",
    "N": "5",
    "R": "6",
}

while True:
    try:
        word = input()
        local = ""
        soundex = ""
        for i in word:
            if letters.get(i, "") != local:
                soundex += letters.get(i, "")
            local = letters.get(i, "")

        print(soundex)
    except EOFError:
        break
