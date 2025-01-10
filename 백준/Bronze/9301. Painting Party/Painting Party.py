for case in range(1, int(input()) + 1):
    N, M = int(input()), int(input())
    paint = [['.' for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        draw, X, Y, W, H, C = input().split()
        X, Y, W, H = int(X), int(Y), int(W), int(H)

        if draw == 'Filled':
            for i in range(N - Y - H + 1, N - Y + 1):
                for j in range(X - 1, X + W - 1):
                    paint[i][j] = C
        else:
            for i in range(N - Y - H + 1, N - Y + 1):
                for j in range(X - 1, X + W - 1):
                    if i in (N - Y - H + 1, N - Y) or j in (X - 1, X + W - 2):
                        paint[i][j] = C

    print(f'Case {case}:')

    for line in paint:
        print(''.join(line))