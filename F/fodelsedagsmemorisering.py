"""Birthday Memorization"""

# fodelsedagsmemorisering

cases = int(input())
birthdays, likeness = {}, {}

for i in range(cases):
    name, like, birthday = input().split()

    if likeness.get(birthday, -1) < int(like):
        likeness[birthday] = int(like)
        birthdays[birthday] = name

print(len(birthdays))

for i in sorted(birthdays.values()):
    print(i)
