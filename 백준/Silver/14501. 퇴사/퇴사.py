N = int(input())
TP, dp = [list(map(int, input().split())) for _ in range(N)], [0 for _ in range(N + 1)]

for i in range(N - 1, -1, -1):
    dp[i] = dp[i + 1] if i + TP[i][0] > N else max(dp[i + 1], dp[i + TP[i][0]] + TP[i][1])

print(dp[0])