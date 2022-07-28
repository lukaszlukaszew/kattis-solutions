"""Head Guard"""

# headguard

while True:
    try:
        line, result = input(), ""
        char, counter = line[0], 1
        for i, val in enumerate(line):
            if i:
                if val == char:
                    counter += 1
                else:
                    result += str(counter) + char
                    char, counter = val, 1

        result += str(counter) + char
        print(result)
    except EOFError:
        break
