"""Simon Says"""

lines = int(input())

for i in range(lines):
    command = input()

    if command.startswith("simon says "):
        print(command.replace("simon says ", ""))
    else:
        print()
