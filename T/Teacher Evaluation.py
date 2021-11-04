"""Teacher Evaluation"""

N, P = [int(x) for x in input().split()]
scores = [int(x) for x in input().split()]

if min(scores) < 100 and P == 100:
    print("Impossible")
else:
    counter = 0
    score = sum(scores)
    while score / (N + counter) < P:
        counter += 1
        score += 100

    print(counter)
