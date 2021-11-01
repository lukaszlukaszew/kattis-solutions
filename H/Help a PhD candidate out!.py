"""Help a PhD candidate out!"""

cases = int(input())

for i in range(cases):
    line = input()
    if line == "P=NP":
        print("skipped")
    else:
        print(eval(line))
