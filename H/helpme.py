"""Help Me With The Game"""

# helpme

from string import ascii_uppercase, ascii_lowercase
from operator import itemgetter

blacks, whites = [], []
white, black = "", ""

for i in range(17):
    line = input()
    if i % 2:
        for j in range(2, 33, 4):
            if line[j] in ascii_lowercase:
                blacks.append(f"{line[j].upper()}{ascii_lowercase[(j-2)//4]}{8 - i // 2}")
            elif line[j] in ascii_uppercase:
                whites.append(f"{line[j]}{ascii_lowercase[(j-2)//4]}{8 - i // 2}")

whites = sorted(whites, key=lambda x: (x[2], x[1]))
blacks = sorted(blacks, key=itemgetter(2), reverse=True)

for figure in "KQRBNP":
    for w in whites:
        if w.startswith(figure):
            white += f'{w.replace("P", "")},'
    for b in blacks:
        if b.startswith(figure):
            black += f'{b.replace("P", "")},'

print("White:", white[:-1])
print("Black:", black[:-1])
