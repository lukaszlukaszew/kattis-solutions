"""Slatkisi"""

price, zeroes = [int(x) for x in input().split()]

bill = int("1" + zeroes * "0")
print(int(((price // bill + int(price - ((price // bill) * bill) >= bill / 2)) * bill)))
