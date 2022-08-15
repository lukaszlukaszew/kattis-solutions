"""ReMorse"""

# remorse

from collections import Counter

symbols = Counter(input().upper().replace(" ", "").replace("?", "").replace("!", "").replace(".", "").replace(',', ""))

result = 3 * (sum(symbols.values()) - 1)
chars, i = [1, 3], 0

for i in range(1, 5):
    temp = chars[-(2**i):]
    for char in temp:
        chars.append(char + 2)
        chars.append(char + 4)

chars.sort(reverse=True)

while symbols:
    for k, v in symbols.items():
        if v == max(symbols.values()):
            result += v * chars.pop()
            symbols.pop(k)
            break

print(result)
