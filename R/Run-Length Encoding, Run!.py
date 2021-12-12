"""Run-Length Encoding, Run!"""


def analyze(line):
    """Analyze message"""
    instr, message = line.split()
    result = ""

    if instr == "E":
        result += message[0]
        letter, count = message[0], 1

        for i in message[1:]:
            if letter == i:
                count += 1
            else:
                result += str(count)
                result += i
                letter, count = i, 1

        result += str(count)

    elif instr == "D":
        for i in range(0, len(message), 2):
            result += message[i] * int(message[i + 1])

    print(result)


analyze(input())
