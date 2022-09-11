"""Thank God it’s Friday"""

# tgif

weekdays = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
duration = {"JAN": 31, "FEB": 28, "MAR": 31, "APR": 30, "MAY": 31,
            "JUN": 30, "JUL": 31, "AUG": 31, "SEP": 30, "OCT": 31,
            "NOV": 30, "DEC": 31}


day, month = input().split()
first_day_of_year = input()
result = []

for i in range(2):
    date = weekdays.index(first_day_of_year)
    for j in range(months.index(month)):
        date += duration[months[j]]
        if months[j] == "FEB":
            date += i

    date += int(day)
    result.append(weekdays[int(date % 7)-1])

chances = result.count("FRI")

if not chances:
    print(":(")
elif chances == 1:
    print("not sure")
elif chances == 2:
    print("TGIF")
