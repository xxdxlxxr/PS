while 1:
    R0, W, C, R = map(int, input().split())

    if R0 + W + C + R == 0:
        break

    print(max(0, (C * W - R0 + R - 1) // R))