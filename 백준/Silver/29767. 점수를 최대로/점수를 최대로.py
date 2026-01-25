N, K = map(int,input().split())
A = list(map(int,input().split()))
dp = [A[0]] + (N - 1) * [0]

for i in range(1, N):
	dp[i] = dp[i - 1] + A[i]
	
print(sum(sorted(dp, reverse=True)[:K]))