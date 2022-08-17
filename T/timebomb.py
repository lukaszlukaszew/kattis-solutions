"""Timebomb"""

# timebomb

digits = {
    "**** ** ** ****": "0",
    "  *  *  *  *  *": "1",
    "***  *****  ***": "2",
    "***  ****  ****": "3",
    "* ** ****  *  *": "4",
    "****  ***  ****": "5",
    "****  **** ****": "6",
    "***  *  *  *  *": "7",
    "**** ***** ****": "8",
    "**** ****  ****": "9",
}

code, number = [], ""

for i in range(5):
    code.append(input())

for i in range(0, len(code[0]), 4):
    digit = ""
    for j in range(5):
        digit += code[j][i: i + 3]

    try:
        number += digits[digit]
    except KeyError:
        print("BOOM!!")
        break

else:
    if int(number) % 6:
        print("BOOM!!")
    else:
        print("BEER!!")
