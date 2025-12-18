for _ in range(int(input())):
    N, i, cnt = int(input()), 5, 0

    while i <= N:
        cnt += N // i
        i *= 5

    print(cnt)