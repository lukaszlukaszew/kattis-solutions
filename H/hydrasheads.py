"""Hydra's Head"""

# hydrasheads

while True:
    H, T = map(int, input().split())

    if H + T:
        counter = 0

        while H + T:
            if H % 2 and not T:
                break

            if H and not H % 2:
                H = H - 2
            elif (not (H + (T / 2)) % 2 and H + T) or (T % 2 == 1 and T > 1):
                H, T = H + 1, T - 2
            elif (H + (T / 2)) % 2 and H + T:
                T = T + 1

            counter += 1

        if H % 2:
            print(-1)
        else:
            print(counter)
    else:
        break
