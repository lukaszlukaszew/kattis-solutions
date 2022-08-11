"""Connect The Dots"""

# connectthedots

from sys import stdin
from string import digits, ascii_lowercase, ascii_uppercase


def connect_the_dots(img, dts):
    """Loops connecting all dots int the image"""
    for a, value in enumerate(order[:-1]):
        if order[a + 1] in dts.keys():
            y, x = dts[value]
            Y, X = dts[order[a + 1]]

            for j in range(min(y, Y), max(y, Y) + int(y == Y)):
                for k in range(min(x, X), max(x, X) + int(x == X)):
                    if img[j][k] == ".":
                        img[j][k] = "-" * int(y == Y) + "|" * int(x == X)
                    elif img[j][k] == "|" and y == Y or img[j][k] == "-" and x == X:
                        img[j][k] = "+"

    for a in img:
        print("".join(a))

    print()


order = digits + ascii_lowercase + ascii_uppercase
image, dots, row = [], {}, 0
line = stdin.readline().rstrip()

while line:
    while line:
        image.append(list(line))
        for i, val in enumerate(line):
            if val != ".":
                dots[val] = (row, i)
        row += 1
        line = stdin.readline().rstrip()
    else:
        connect_the_dots(image, dots)
        image, dots, row = [], {}, 0
        line = stdin.readline().rstrip()
else:
    connect_the_dots(image, dots)
