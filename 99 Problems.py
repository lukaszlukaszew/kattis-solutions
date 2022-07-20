"""99 Problems"""

# 99problems

from collections import defaultdict

result = defaultdict(list)
price = int(input())

result[abs(price - (price//100 * 100 + 99))].append(price//100 * 100 + 99)

if (price//100 - 1) * 100 + 99 > 0:
    result[abs(price - ((price//100 - 1) * 100 + 99))].append((price//100 - 1) * 100 + 99)

print(max(result[min(result.keys())]))
