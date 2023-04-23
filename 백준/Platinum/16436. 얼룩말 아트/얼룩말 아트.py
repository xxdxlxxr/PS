W, H, K = map(int, input().split())
board1, board2, image1, image2 = [2501 * [0] for _ in range(2501)], [5001 * [0] for _ in range(5001)], [2501 * [0] for _ in range(2501)], [5001 * [0] for _ in range(5001)]

for _ in range(K):
    info = list(map(int, input().split()))

    if info[0] == 1:
        px, py, qx, qy = info[1:]

        board1[px][py] += 1
        board1[px][qy + 1] -= 1
        board1[qx + 1][py] -= 1
        board1[qx + 1][qy + 1] += 1
    else:
        px, py, r = info[1:]

        board2[px - py - r + 2500][px - r + py] += 1
        board2[px - py - r + 2500][px + r + py + 1] -= 1
        board2[px - py + r + 2501][px - r + py] -= 1
        board2[px - py + r + 2501][px + r + py + 1] += 1

image1[0][0], image2[0][0] = board1[0][0], board2[0][0]

for i in range(2500):
    image1[0][i], image1[i][0] = image1[0][i - 1] + board1[0][i], image1[i - 1][0] + board1[i][0]

for i in range(2500):
    for j in range(2500):
        image1[i][j] = image1[i - 1][j] + image1[i][j - 1] - image1[i - 1][j - 1] + board1[i][j]

for i in range(5000):
    image2[0][i], image2[i][0] = image2[0][i - 1] + board2[0][i], image2[i - 1][0] + board2[i][0]

for i in range(5000):
    for j in range(5000):
        image2[i][j] = image2[i - 1][j] + image2[i][j - 1] - image2[i - 1][j - 1] + board2[i][j]

for j in range(H):
    for i in range(W):
        if (image1[i][j] + image2[i - j + 2500][i + j]) % 2:
            print('#', end = '')
        else:
            print('.', end = '')

    print()