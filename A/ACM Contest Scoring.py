"""ACM Contest Scoring"""

# acm

penalties = {}
solved = 0
points = 0

while True:
    try:
        m, n, r = input().split()

        if r == "wrong":
            penalties[n] = penalties.get(n, 0) + 1
        else:
            points += int(m) + 20 * penalties.get(n, 0)
            solved += 1

    except ValueError:
        print(solved, points)
        break
