"""Hanging Out on the Terrace"""

L, x = map(int, input().split())
current, blocked = 0, 0

for i in range(x):
    instr, p = input().split()
    if instr == "enter":
        blocked += int(current + int(p) > L)
        current += int(p) * int(current + int(p) <= L)
    elif instr == "leave":
        current -= int(p)

print(blocked)
