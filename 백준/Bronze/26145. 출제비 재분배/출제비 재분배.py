N, M = map(int, input().split())
S = list(map(int, input().split()))
answer = [0 for _ in range(N + M)]

for i in range(N):
    T = list(map(int, input().split()))

    for j in range(N + M):
        if i == j:
            answer[j] += S[j] - sum(T)
        else:
            answer[j] += T[j]

print(*answer)