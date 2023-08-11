for _ in range(int(input())):
    N, D = map(int, input().split())
    cnt = 0

    for _ in range(N):
        v, f, c = map(int, input().split())
        cnt += D * c <= v * f

    print(cnt)