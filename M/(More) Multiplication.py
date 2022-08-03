"""(More) Multiplication"""

# multiplication

x, y = input().split()

while int(x) + int(y):
    check = []
    result = int(x) * int(y)

    for i in range(4 * len(y) + 5):
        if i in (0, 4 * len(y) + 4):
            line = "+-" + 4 * len(x) * "-" + "--+"
        elif i == 1:
            line = "| "
            for j, val in enumerate(x):
                line += "  " + val + " "
            line += "  |"
        elif i == 4 * len(y) + 3:
            line = "|"
            ind = int(i // 4) - 1 + len(str(result)) - len(x) - len(y)
            for j, val in enumerate(x):
                if ind < 0:
                    line += "  "
                else:
                    line += "/ "
                line += str(result)[-len(x):][j] + " "
                ind += 1
            line += "   |"
        elif i % 4 == 1:
            line = "|"
            ind = int(i // 4) - 1 + len(str(result)) - len(x) - len(y)
            if ind < 0:
                line += " "
            else:
                line += str(result)[ind]
            for j, val in enumerate(x):
                line += "|/ " + str(int(y[int(i // 4) - 1]) * int(val))[-1]
            line += "| |"
        elif i % 4 == 2:
            line = "| " + len(x) * "+---" + "+ |"
        elif i % 4 == 3:
            line = "|"
            ind = int(i // 4) - 1 + len(str(result)) - len(x) - len(y)
            if ind < 0:
                line += " "
            else:
                line += "/"
            for j, val in enumerate(x):
                line += "|" + str(int(y[int(i // 4)]) * int(val)).zfill(2)[0] + " /"
            line += "| |"
        elif i % 4 == 0:
            line = "| " + len(x) * "| / " + "|" + y[int(i // 4) - 1] + "|"

        print(line)

    print()

    x, y = input().split()
