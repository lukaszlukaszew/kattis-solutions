"""Akcija"""

# akcija

books = int(input())
prices = []

for i in range(books):
    prices.append(int(input()))

prices.sort(reverse=True)

print(sum(prices) - sum(prices[2::3]))
