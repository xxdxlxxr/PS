import sys

input = sys.stdin.readline
inf = float('inf')
input()
N, M, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(K):
    u, v, c, d = map(int, input().split())
    graph[u].append((v, c, d))

dp = [[inf for _ in range(N + 1)] for _ in range(M + 1)]
dp[0][1] = 0

for i in range(M + 1):
    for j in range(1, N + 1):
        if dp[i][j] != inf:
            for v, c, d in graph[j]:
                if i + c <= M:
                    dp[i + c][v] = min(dp[i + c][v], dp[i][j] + d)

answer = min(dp[i][N] for i in range(M + 1))
print(answer if answer != inf else 'Poor KCM')