"""Fifty Shades of Pink"""

# fiftyshades

COUNTER = 0
words = ["pink", "rose"]

for i in range(int(input())):
    word = input().lower()
    for j in words:
        if j in word:
            COUNTER += 1
            break

if COUNTER:
    print(COUNTER)
else:
    print("I must watch Star Wars with my daughter")
