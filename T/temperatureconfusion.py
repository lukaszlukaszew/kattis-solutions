"""Temperature Confusion"""

# temperatureconfusion


def nwd(a, b):
    """greatest common divisor"""
    while b:
        a, b = b, a % b
    return a


fnumerator, fdenominator = map(int, input().split("/"))
cnumerator, cdenominator = -32, 1

if fdenominator != cdenominator:
    fnumerator, fdenominator, cnumerator, cdenominator = (
        fnumerator * cdenominator,
        fdenominator * cdenominator,
        cnumerator * fdenominator,
        cdenominator * fdenominator,
    )

cnumerator, cdenominator = (fnumerator + cnumerator) * 5, cdenominator * 9
cnwd = nwd(cnumerator, cdenominator)

print(str(int(cnumerator / cnwd)) + "/" + str(int(cdenominator / cnwd)))
