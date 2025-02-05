while 1:
    N = int(input())

    if not N:
        break

    print(N * (N + 1) * (2 * N + 1) // 6)