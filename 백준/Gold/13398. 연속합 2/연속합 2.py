n, A = int(input()), list(map(int, input().split()))
dp = [[num for num in A] for _ in range(2)]

for i in range(1, n):
    dp[0][i] = max(dp[0][i - 1] + A[i], dp[0][i])
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + A[i])
    
print(max(dp[0] + dp[1]))