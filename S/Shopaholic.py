"""Shopaholic"""

# shopaholic

from sys import stdin

items = int(input())
prices = sorted([int(x) for x in stdin.readline().split()], reverse=True)
print(sum(prices[2::3]))
