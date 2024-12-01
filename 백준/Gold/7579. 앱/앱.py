N, M = map(int, input().split())
tmp, cost = [0] + list(map(int, input().split())), [0] + list(map(int, input().split()))
max_cost = sum(cost)
dp, answer = [[0] * (max_cost + 1) for _ in range(N + 1)], max_cost

for i in range(1, N + 1):
    for j in range(max_cost + 1):
        if j >= cost[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i]] + tmp[i])
        else:
            dp[i][j] = dp[i - 1][j]

        if dp[i][j] >= M:
            answer = min(j, answer)

print(answer)