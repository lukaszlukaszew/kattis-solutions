"""Turn It Up!"""

# skruop

vol = 7

for i in range(int(input())):
    line = input()
    if line == "Skru op!":
        vol = min(vol + 1, 10)
    else:
        vol = max(vol - 1, 0)

print(vol)
