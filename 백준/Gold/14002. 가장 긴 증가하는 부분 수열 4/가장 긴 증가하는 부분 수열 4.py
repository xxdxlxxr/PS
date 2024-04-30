N, A = int(input()), list(map(int, input().split()))
dp = N * [1]

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

M = max(dp)

print(M)

answer = []

for i in range(N - 1, -1, -1):
    if dp[i] == M:
        answer.insert(0, A[i])
        M -= 1

print(*answer)