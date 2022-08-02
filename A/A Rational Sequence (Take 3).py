"""A Rational Sequence (Take 3)"""

# rationalsequence3


def sequence(position):
    """Produce sequence of needed to get to desired position"""
    jumps, left_outer, level = "", 1, 0

    while position > left_outer:
        level += 1
        left_outer += 2 ** level

    left = left_outer - 2 ** level + 1
    right = left_outer
    middle = int((left + right) / 2)

    for _ in range(level):
        if position > middle:
            jumps += "R"
            left = middle
        else:
            jumps += "L"
            right = middle

        middle = int((left + right) / 2)

    return jumps


cases = int(input())

for i in range(cases):
    case, desired = [int(x) for x in input().split()]
    p, q = 1, 1

    for j in sequence(desired):
        if j == "R":
            p = p + q
        elif j == "L":
            q = (p + q)

    print(case, str(p) + "/" + str(q))
