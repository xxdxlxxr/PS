N, A = int(input()), list(map(int, input().split()))
dp = N * [N + 1]
dp[0] = 0

for i in range(N):
    for j in range(1, A[i] + 1):
        if i + j < N:
            dp[i + j] = min(dp[i] + 1, dp[i + j])

print(-1 if dp[N - 1] == N + 1 else dp[N - 1])