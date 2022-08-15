"""Guessing Game"""

# guessinggame

full_range = range(1, 11)
num = int(input())

while num:
    command = input()

    if command == "too high":
        full_range = list(filter(lambda x: x < num, full_range))
    elif command == "too low":
        full_range = list(filter(lambda x: x > num, full_range))
    else:
        if num in list(full_range):
            print("Stan may be honest")
        else:
            print("Stan is dishonest")

        full_range = range(1, 11)

    num = int(input())
