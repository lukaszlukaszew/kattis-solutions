"""Star Arrangements"""

S = int(input())
print(str(S) + ":")

for i in range(2, S):
    for j in range(i - 1, i + 1):
        c = 0
        while c < S:
            c += i
            if c == S:
                break
            c += j
        if c == S:
            print(f"{i},{j}")
