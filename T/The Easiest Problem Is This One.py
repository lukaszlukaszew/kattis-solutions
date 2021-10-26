"""The Easiest Problem Is This One"""

num = int(input())

while num:
    summary = sum(map(int, str(num)))

    for i in range(11, 101):
        summary_extended = sum(map(int, str(num*i)))

        if summary == summary_extended:
            print(i)
            break

    num = int(input())
