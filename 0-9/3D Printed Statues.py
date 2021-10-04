"""3D Printed Statues"""

D = 0
a = int(input())

while a > 2 ** D:
    D += 1

print(D + 1)
