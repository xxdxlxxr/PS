N, M = map(int, input().split())
baskets = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j, k = map(int, input().split())
    baskets = baskets[:i - 1] + baskets[k - 1:j] + baskets[i - 1:k - 1] + baskets[j:]

print(*baskets)