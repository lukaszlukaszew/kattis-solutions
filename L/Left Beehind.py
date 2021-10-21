"""Left Beehind"""

while True:
    x, y = map(int, input().split())

    if x + y:
        if x + y == 13:
            print('Never speak again.')
        elif x > y:
            print('To the convention.')
        elif x < y:
            print('Left beehind.')
        elif x == y:
            print('Undecided.')
    else:
        break
