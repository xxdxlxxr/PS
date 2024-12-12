N, K = map(int, input().split())
K %= 10
nums = [i for i in range(1, N + 1) if i % 10 not in (K, (2 * K) % 10)]
print(len(nums))
print(*nums)