"""Popular Vote"""

cases = int(input())

for i in range(cases):
    candidates = int(input())
    votes = []

    for j in range(candidates):
        votes.append(int(input()))

    if max(votes) == min(votes) or votes.count(max(votes)) > 1:
        print("no winner")
    elif max(votes) / sum(votes) > 0.5:
        print("majority winner", votes.index(max(votes)) + 1)
    else:
        print("minority winner", votes.index(max(votes)) + 1)
