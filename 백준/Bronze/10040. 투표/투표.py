N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
B = [int(input()) for _ in range(M)]

cnt, max_vote, answer = N * [0], 0, -1

for i in range(M):
    for j in range(N):
        if A[j] <= B[i]:
            cnt[j] += 1
            break

for i in range(N):
    if max_vote < cnt[i]:
        max_vote = cnt[i]
        answer = i

print(answer + 1)