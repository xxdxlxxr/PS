N, K, P = map(int, input().split())
bread = list(map(int, input().split()))
print(N - sum(b.count(0) >= P for b in [bread[i * K:(i + 1) * K] for i in range((len(bread) + K - 1) // K)]))