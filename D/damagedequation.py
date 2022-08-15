"""Damaged Equation"""

# damagedequation

operators = ["*", "+", "-", "/"]

a, b, c, d = input().split()
e, f = "int(", ")"
counter = 0

for i in operators:
    for j in operators:
        try:
            if eval(e + a + i + b + f) == eval(e + c + j + d + f):
                print(a, i, b, "=", c, j, d)
                counter += 1
        except ZeroDivisionError:
            continue

if not counter:
    print("problems ahead")
