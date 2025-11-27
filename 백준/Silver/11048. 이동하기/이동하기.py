N, M = map(int, input().split())
dp, candy = (N + 1) * [[0] * (M + 1)], [list(map(int, input().split())) for i in range(N)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + candy[i - 1][j - 1]

print(dp[N][M])