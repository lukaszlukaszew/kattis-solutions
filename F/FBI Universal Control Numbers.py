"""FBI Universal Control Numbers"""

# fbiuniversal

digits = "0123456789ACDEFHJKLMNPRTVWX"
mistakes = {
    "B": "8",
    "G": "C",
    "I": "1",
    "O": "0",
    "Q": "0",
    "S": "5",
    "U": "V",
    "Y": "V",
    "Z": "2",
}
comp = [2, 4, 5, 7, 8, 10, 11, 13]

cases = int(input())

for i in range(cases):
    case, num = input().split()
    dec, res = 0, 0
    for j in range(8):
        dec += digits.index(mistakes.get(num[j], num[j])) * comp[j]
        res += digits.index(mistakes.get(num[j], num[j])) * 27 ** (7 - j)

    if digits[int(dec % 27)] == num[-1]:
        print(case, res)
    else:
        print(case, "Invalid")
