N, M = map(int, input().split())
L, cnt = list(map(int, input().split())), 0

for _ in range(N - 1):
    K, total = list(map(int, input().split())), 0

    for i in range(M):
        total += abs(L[i] - K[i])

    cnt += total > 2000

    if 2 * cnt + 1 >= N:
        print('YES')
        break
else:
    print('NO')