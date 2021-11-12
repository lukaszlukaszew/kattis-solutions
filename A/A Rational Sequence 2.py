"""A Rational Sequence 2"""

test_cases = int(input())

for i in range(test_cases):
    line = input()
    p, q = [int(x) for x in line[line.index(" ") + 1:].split("/")]

    sequence = ""

    while p > 1 or q > 1:
        if q > p:
            q -= p
            sequence += "L"
        else:
            p -= q
            sequence += "R"

    n = 1

    for j in sequence[::-1]:
        n *= 2
        if j == "R":
            n += 1

    print(i + 1, n)
