"""Help a PhD candidate out!"""

# helpaphd

cases = int(input())

for i in range(cases):
    line = input()
    if line == "P=NP":
        print("skipped")
    else:
        print(eval(line))
