def dfs(idx):
    global visited
    visited[idx] = True
    print(idx, end=' ')

    for next in range(1, N + 1):
        if not visited[next] and graph[idx][next]:
            dfs(next)

def bfs():
    global q, visited

    while q:
        cur = q.pop(0)
        print(cur, end=' ')

        for next in range(1, N + 1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)

N, M, V = map(int, input().split())
graph = [(N + 1) * [False] for _ in range(N + 1)]
visited = (N + 1) * [False]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b], graph[b][a] = True, True

dfs(V)
print()

visited = (N + 1) * [False]
q = [V]
visited[V] = True
bfs()