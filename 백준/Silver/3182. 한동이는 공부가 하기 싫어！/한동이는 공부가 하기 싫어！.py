N = int(input())
graph, answer = [0] + [int(input()) for _ in range(1, N + 1)], [0]

def dfs(start):
    visit[start] = True

    if not visit[graph[start]]:
        dfs(graph[start])

for i in range(1, N + 1):
    visit = (N + 1) * [False]
    dfs(i)
    answer.append(visit.count(True))

print(answer.index(max(answer)))