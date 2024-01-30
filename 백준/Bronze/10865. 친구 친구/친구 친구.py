N, M = map(int, input().split())
cnt = M * [0]

for _ in range(M):
    A, B = map(int, input().split())
    cnt[A - 1] += 1
    cnt[B - 1] += 1

for i in range(N):
    print(cnt[i])