from sys import stdin

cases = int(stdin.readline())

for i in range(cases):
    result = 0
    teams = int(stdin.readline())
    scores = sorted(list(map(int, stdin.readline().split())), reverse = True)

    for j in range(teams):
        result += scores[1+j*2]

    print(result)
