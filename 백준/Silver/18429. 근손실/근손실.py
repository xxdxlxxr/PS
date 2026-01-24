def find(x,n):
    global answer

    if x < 500:
        return
    
    if n == N:
        answer += 1
        return 
    
    x -= K

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            find(x + A[i], n + 1)
            visited[i] = 0

N, K = map(int, input().split())
A = list(map(int, input().split()))
answer, visited = 0, N * [0]
find(500, 0)
print(answer)