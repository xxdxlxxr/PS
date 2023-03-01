from itertools import combinations

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
answer = 0

for com in combinations(range(M), 3):
    sum = 0

    for i in range(N):
        a = 0

        for j in com:
            a = max(a, A[i][j])

        sum += a

    answer = max(answer, sum)

print(answer)