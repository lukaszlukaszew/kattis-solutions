"""Genetic Search"""

# geneticsearch

import re

line = input()

while line != "0":
    S, L = line.split()
    result = [0, 0, 0]

    result[0] = len(re.findall(f"(?={S})", L))

    S = list(S)
    second_step = set()

    for i, _ in enumerate(S):
        s = "".join(S[:i] + S[i + 1 :])

        if s in second_step:
            continue

        second_step.add(s)
        result[1] += len(re.findall(f"(?={s})", L))

    third_step = set()
    letters = ["A", "G", "C", "T"]

    for i in range(len(S) + 1):
        for letter in letters:
            S.insert(i, letter)
            s = "".join(S)
            del S[i]

            if s in third_step:
                continue

            third_step.add(s)
            result[2] += len(re.findall(f"(?={s})", L))

    print(*result)

    line = input()
