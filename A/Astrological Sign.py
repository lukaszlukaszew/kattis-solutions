"""Astrological Sign"""

signs = {
    "Jan": (21, "Capricorn", "Aquarius"),
    "Feb": (20, "Aquarius", "Pisces"),
    "Mar": (21, "Pisces", "Aries"),
    "Apr": (21, "Aries", "Taurus"),
    "May": (21, "Taurus", "Gemini"),
    "Jun": (22, "Gemini", "Cancer"),
    "Jul": (23, "Cancer", "Leo"),
    "Aug": (23, "Leo", "Virgo"),
    "Sep": (22, "Virgo", "Libra"),
    "Oct": (23, "Libra", "Scorpio"),
    "Nov": (23, "Scorpio", "Sagittarius"),
    "Dec": (22, "Sagittarius", "Capricorn"),
}


cases = int(input())

for i in range(cases):
    day, month = input().split()

    print(signs[month][1 + int(int(day) >= signs[month][0])])
