"""Eligibility"""

cases = int(input())

for i in range(cases):
    record = input().split()

    if int(record[1][:4]) >= 2010 or int(record[2][:4]) >= 1991:
        print(record[0], "eligible")
    elif int(record[3]) >= 41:
        print(record[0], "ineligible")
    else:
        print(record[0], "coach petitions")
