while 1:
    N, M = map(int, input().split())

    if not N and not M:
        break

    A, answer = list(map(int, input().split())), 0

    for i in range(N):
        answer += min(A[i], M // N)

    print(answer)