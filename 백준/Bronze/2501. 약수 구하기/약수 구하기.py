N, K = map(int, input().split())
numbers = [i for i in range(1, N + 1) if N % i == 0]
print(0 if len(numbers) < K else numbers[K - 1])