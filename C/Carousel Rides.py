"""Carousel Rides"""

while True:
    n, m = [int(x) for x in input().split()]
    best_offer = [0, 0, 0]

    if n or m:
        for i in range(n):
            count, price = [int(x) for x in input().split()]
            ratio = price / count

            if count <= m:
                if (
                    not sum(best_offer)
                    or ratio < best_offer[0]
                    or (ratio == best_offer[0] and best_offer[1] < count)
                ):
                    best_offer = [ratio, count, price]

        if sum(best_offer):
            print(f"Buy {best_offer[1]} tickets for ${best_offer[2]}")
        else:
            print("No suitable tickets offered")
    else:
        break
