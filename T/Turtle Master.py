"""Turtle Master"""

b = []

for i in range(8):
    b.append(list(input()))

instruction = input()

m = {"up": (0, -1), "right": (1, 0), "down": (0, 1), "left": (-1, 0)}
d, t = "right", [0, 7]

for i in instruction:
    if i == "R":
        d = list(m.keys())[(list(m.keys()).index(d) + 1) % 4]
    elif i == "L":
        d = list(m.keys())[(list(m.keys()).index(d) - 1) % 4]
    elif b[t[1] + m[d][1]][t[0] + m[d][0]] == "I" and i == "X":
        b[t[1] + m[d][1]][t[0] + m[d][0]] = "."
    elif b[t[1] + m[d][1]][t[0] + m[d][0]] in ".D" and i == "F":
        t = [t[0] + m[d][0], t[1] + m[d][1]]
    else:
        print("Bug!")
        break
else:
    if b[t[1]][t[0]] == "D":
        print("Diamond!")
    else:
        print("Bug!")
