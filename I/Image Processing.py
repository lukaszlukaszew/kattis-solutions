"""Image Processing"""

H, W, N, M = [int(x) for x in input().split()]

image = []
kernel = []

for i in range(H):
    image.append([int(x) for x in input().split()])

for i in range(N):
    kernel.append([int(x) for x in input().split()])

last_one = []

for i in range(H - N + 1):
    row = []
    for j in range(W - M + 1):
        result = 0

        for k in range(N):
            for l in range(M):
                result += image[i + k][j + l] * kernel[N - k - 1][M - l - 1]

        row.append(str(result))
    last_one.append(row)

for row in last_one:
    print(" ".join(row))
