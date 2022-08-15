"""Ptice"""

# ptice

N = int(input())
answers = input()

strings = {
    "Adrian": "ABC" * ((N // 3) + 1),
    "Bruno": "BABC" * ((N // 4) + 1),
    "Goran": "CCAABB" * ((N // 6) + 1),
}
scores = {"Adrian": 0, "Bruno": 0, "Goran": 0}

for i in range(N):
    for k, v in strings.items():
        if v[i] == answers[i]:
            scores[k] += 1

print(max(scores.values()))
for k, v in scores.items():
    if v == max(scores.values()):
        print(k)
