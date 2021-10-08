"""A New Alphabet"""

alphabet = {
    "a": "@",
    "b": "8",
    "c": "(",
    "d": "|)",
    "e": "3",
    "f": "#",
    "g": "6",
    "h": "[-]",
    "i": "|",
    "j": "_|",
    "k": "|<",
    "l": "1",
    "m": r"[]\/[]",
    "n": r"[]\[]",
    "o": "0",
    "p": "|D",
    "q": "(,)",
    "r": "|Z",
    "s": "$",
    "t": "']['",
    "u": "|_|",
    "v": r"\/",
    "w": r"\/\/",
    "x": "}{",
    "y": "`/",
    "z": "2",
}

line = input().lower()
result = ""

for i in line:
    result += alphabet.get(i, i)

print(result)
