"""Simon Says"""

lines = int(input())

for i in range(lines):
    command = input()

    if command.startswith("Simon says "):
        print(command.replace("Simon says ", ""))
