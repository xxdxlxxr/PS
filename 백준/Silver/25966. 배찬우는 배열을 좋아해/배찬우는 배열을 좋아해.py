N, M, q = map(int, input().split())
answer = []

for _ in range(N):
    answer.append(list(map(int, input().split())))

for _ in range(q):
    query = list(map(int, input().split()))

    if query[0]:
        answer[query[1]], answer[query[2]] = answer[query[2]], answer[query[1]]
    else:
        answer[query[1]][query[2]] = query[3]

for arr in answer:
    print(*arr)
