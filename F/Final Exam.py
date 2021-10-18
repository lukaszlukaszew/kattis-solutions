"""Final Exam"""

questions = int(input())
counter, local = 0, ""

for i in range(questions):
    if not local:
        local = input()
    else:
        next_one = input()
        counter += int(local == next_one)
        local = next_one

print(counter)
