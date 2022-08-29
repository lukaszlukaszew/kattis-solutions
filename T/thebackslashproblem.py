"""The Backslash Problem"""

# thebackslashproblem

while True:
    try:
        iterations = int(input())
        line = list(input())
        result = []

        for i in range(iterations):
            if i % 2:
                line = []
                for j in result:
                    if (ord(j) in range(33, 43)) or (ord(j) in (91, 92, 93)):
                        line.append(chr(92))
                    line.append(j)
            else:
                result = []
                for j in line:
                    if (ord(j) in range(33, 43)) or (ord(j) in (91, 92, 93)):
                        result.append(chr(92))
                    result.append(j)

        print("".join(result)) if len(result) > len(line) else print("".join(line))

    except EOFError:
        break
