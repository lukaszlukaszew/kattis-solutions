"""Bluetooth"""

sides = {False: ("+_", "-_"), True: ("_+", "_-")}
jaw = {"+_": set(), "_+": set(), "-_": set(), "_-": set()}

for i in ("+", "-"):
    for j in range(1, 9):
        jaw[i + "_"].add(i + str(j))
        jaw["_" + i].add(str(j) + i)

tooths = int(input())
for i in range(tooths):
    tooth, defect = input().split()
    if defect == "m":
        for j, val in jaw.items():
            val.discard(tooth)
    else:
        for val in sides[tooth[0].isnumeric()]:
            if jaw.get(val, 0):
                jaw.pop(val)

if jaw.get("+_", 0) and jaw.get("-_", 0):
    print(0)
elif jaw.get("_+", 0) and jaw.get("_-", 0):
    print(1)
else:
    print(2)
