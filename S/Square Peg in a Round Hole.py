"""Square Peg in a Round Hole"""

N, M, K = [int(x) for x in input().split()]
plots = sorted(int(x) for x in input().split())
houses = [int(x) for x in input().split()]
houses += [float(int(x) * (1 / 2) ** (1 / 2)) for x in input().split()]

houses.sort()
counter = 0

while houses and plots:
    if houses[-1] < plots[-1]:
        plots.pop()
        counter += 1

    houses.pop()

print(counter)
