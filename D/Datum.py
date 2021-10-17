"""Datum"""

from datetime import date

day, month = map(int, input().split())
print(date(2009, month, day).strftime("%A"))
