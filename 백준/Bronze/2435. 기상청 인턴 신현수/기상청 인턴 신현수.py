N, K = map(int, input().split())
temp = list(map(int, input().split()))

print(max(sum(temp[i:i + K]) for i in range(N - K + 1)))