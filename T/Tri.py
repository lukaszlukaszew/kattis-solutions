"""Tri"""

# tri

x, y, z = input().split()
operators = ["-", "+", "*", "/"]

for operator in operators:
    if eval(x + operator + y) == int(z):
        print(x + operator + y + "=" + z)
        break
    if int(x) == eval(y + operator + z):
        print(x + "=" + y + operator + z)
        break
