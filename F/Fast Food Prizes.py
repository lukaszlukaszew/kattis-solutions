"""Fast Food Prizes"""

cases = int(input())

for i in range(cases):
    prizes, sticker_types = [int(x) for x in input().split()]
    prize_stickers, stickers = {}, {}
    prize = 0

    for j in range(prizes):
        line = [int(x) for x in input().split()]
        prize_stickers[tuple(line[1:-1])] = line[-1]

    line = [int(x) for x in input().split()]

    for j in range(sticker_types):
        stickers[j + 1] = line[j]

    for key, val in prize_stickers.items():
        prize += min([stickers[x] for x in key]) * val

    print(int(prize))
