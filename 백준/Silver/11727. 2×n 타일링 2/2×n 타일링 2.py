dp = [1, 1]

for _ in range(1000 - 1):
    dp.append(2 * dp[-2] + dp[-1])

print(dp[int(input())] % 10007)