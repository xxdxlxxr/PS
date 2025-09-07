dp = [0, 1, 1]

for i in range(10000 - 2):
    dp.append(dp[-2] + dp[-1])

for i in range(1, int(input()) + 1):
    P, Q = map(int, input().split())
    print(f'Case #{i}: {dp[P] % Q}')