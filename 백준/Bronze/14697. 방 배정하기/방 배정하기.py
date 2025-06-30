A, B, C, N = list(map(int, input().split()))
dp = (300 + 1) * [0]
dp[A] = dp[B] = dp[C] = 1

for i in range(A, N + 1):
   for j in [A, B, C]:
      if i >= j and dp[i - j]:
         dp[i] = 1

print(dp[N])