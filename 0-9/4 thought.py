"""4 thoughts"""

# 4thought

operators = ["+", "-", "*", "//"]
possibilities = []

for i in operators:
    for j in operators:
        for k in operators:
            possibilities.append((i, j, k))

test_cases = int(input())

for j in range(test_cases):
    result = int(input())

    finish = ""

    for i in possibilities:
        if eval("4" + i[0] + "4" + i[1] + "4" + i[2] + "4") == result:
            finish = "4 " + i[0] + " 4 " + i[1] + " 4 " + i[2] + " 4 = " + str(result)
            finish = finish.replace("//", "/")
            break

    if finish == "":
        finish = "no solution"

    print(finish)
