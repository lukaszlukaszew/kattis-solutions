"""What does the fox say?"""

cases = int(input())

for i in range(cases):
    voices, result = [], []
    recording = input().split()

    while True:
        explanation = input().split()
        voices.append(explanation[-1])
        if explanation[0] == "what":
            break

    result = []
    for j, val in enumerate(recording):
        if val in voices:
            continue

        result.append(val)

    print(*result)
