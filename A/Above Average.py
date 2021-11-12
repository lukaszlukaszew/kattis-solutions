"""Above Average"""

cases = int(input())

for i in range(cases):
    case = [int(x) for x in input().split()]

    while case[0] != len(case[1:]):
        case.extend(*list(map(int, input().split())))

    avg = (sum(case) - case[0]) / case[0]
    above = len(list(filter(lambda x: x > avg, case[1:])))

    result = above * 100 / case[0]

    print(format(result, ".3f") + "%")
