"""FizzBuzz"""

X, Y, N = map(int, input().split())

for i in range(1, N + 1):
    if not i % X:
        if not i % Y:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif not i % Y:
        print("Buzz")
    else:
        print(i)
