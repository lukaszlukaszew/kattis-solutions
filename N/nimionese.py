"""Nimionese"""

# nimionese

consonants = "bcdgknpt"


def hard_consonant(letter):
    """Prepare proper hard consonant switch"""
    possibilities = []

    if letter.isupper():
        letters = consonants.upper()
    else:
        letters = consonants

    if letter.lower() not in letters:
        for consonant in letters:
            possibilities.append((abs(ord(letter) - ord(consonant)), abs(ord(consonant) - ord("A")), consonant))

        possibilities.sort()

        if letter.isupper():
            letter = possibilities[0][2].upper()
        else:
            letter = possibilities[0][2]

    return letter


def ending(letter):
    """Prepare proper ending of the word"""
    first_ending_letter = "aou"
    if letter.lower() in consonants:
        possibilities = []
        for fel in first_ending_letter:
            possibilities.append((abs(ord(letter) - ord(fel)), abs(ord(fel) - ord("A")), fel + "h"))

        possibilities.sort()
        full_ending = possibilities[0][2]

    else:
        full_ending = ""

    return full_ending


line = input().split()

for i, elem in enumerate(line):
    syllabes = elem.split("-")

    syllabes[0] = hard_consonant(syllabes[0][0]) + syllabes[0][1:]
    hard = hard_consonant(syllabes[0][0]).lower()

    for z in range(len(syllabes[1:])):
        for y in "bcdgknpt":
            syllabes[z + 1] = syllabes[z + 1].replace(y, hard)

    syllabes[-1] = syllabes[-1] + ending(syllabes[-1][-1])

    line[i] = "".join(syllabes)

print(*line)
