"""Text Messaging Outrage"""

# textmessaging

from sys import stdin

cases = int(stdin.readline())

for i in range(cases):
    RESULT = 0
    P, K, L = [int(x) for x in stdin.readline().split()]
    letters = sorted(map(int, stdin.readline().split()), reverse=True)

    for j in range(P):
        RESULT += (j + 1) * sum(letters[j * K: (j + 1) * K])
        print()

    print(f"Case #{i+1}: {RESULT}")
