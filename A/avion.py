"""Avion"""

# avion

result = ""

for i in range(5):
    if "FBI" in input():
        result += str(i + 1) + " "

if result:
    print(result)
else:
    print("HE GOT AWAY!")
