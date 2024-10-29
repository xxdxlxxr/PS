N, M = map(int, input().split())
A = list(reversed(list(map(int, input().split()))))

for i in range(N - 1):
    A[i + 1] += A[i]

    if A[i + 1] >= M:
        print(N - i - 1)
        break
else:
    print(-1)