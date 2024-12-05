N, M = map(int, input().split())
A = list(reversed(list(map(int, input().split()))))
total = 0

for i in range(N):
    total += A[i]

    if total >= M:
        print(N - i)
        break
else:
    print(-1)