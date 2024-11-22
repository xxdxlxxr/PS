N, K = map(int, input().split())
cnt = [7 * [0] for _ in range(2)]

for _ in range(N):
    S, Y = map(int, input().split())
    cnt[S][Y] += 1

print(sum(y // K + (y % K != 0) for s in cnt for y in s[1:]))