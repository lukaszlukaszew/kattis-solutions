"""UTF-8"""

# utf8

n = int(input())
bytes_list = []
types = {0: 0, 1: 0, 2: 0, 3: 0}
counter = 0

for i in range(n):
    bytes_list.append(input())

for i, val in enumerate(bytes_list):
    if counter:
        if val.startswith("10"):
            counter -= 1
        else:
            print("invalid")
            break
    else:
        if val.startswith("0"):
            types[0] += 1
        elif val.startswith("110"):
            counter = 1
            types[1] += 1
        elif val.startswith("1110"):
            counter = 2
            types[2] += 1
        elif val.startswith("11110"):
            counter = 3
            types[3] += 1
        else:
            print("invalid")
            break
else:
    if counter:
        print("invalid")
    else:
        for i in range(4):
            print(types[i])
