N, M = map(int, input().split())
front, back = [], []

for _ in range(N):
    A, B = map(int, input().split())
    front.append(A)
    back.append(B)

for _ in range(M):
    K = int(input())

    for i in range(N):
        if front[i] <= K:
            front[i], back[i] = back[i], front[i]

print(sum(front))