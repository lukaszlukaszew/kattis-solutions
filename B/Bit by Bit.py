"""Bit by Bit"""

# bitbybit

to_map = {None: "?", True: "1", False: "0"}


def check(instr, x, y):
    """Compare bits"""
    if instr == "AND":
        if register[x] is None and register[y] is False:
            register[x] = False
        else:
            register[x] = register[x] and register[y]
    elif instr == "OR":
        if register[x] is None and register[y] is False:
            register[x] = None
        else:
            register[x] = register[x] or register[y]


instructions = int(input())

while instructions:
    register = [None for x in range(32)]

    for i in range(instructions):
        instruction, *bits = input().split()

        if instruction == "SET":
            register[int(bits[0])] = True
        elif instruction == "CLEAR":
            register[int(bits[0])] = False
        else:
            check(instruction, *list(map(int, bits)))

    print("".join(list(map(lambda x: to_map[x], register[::-1]))))

    instructions = int(input())
