N, M = map(int, input().split())

for i in range(N):
    print(*list(range(i * M + 1, i * M + M + 1)))