N, M = map(int, input().split())

for i in range(N):
    for j in range(M):
        print('*.'[(i + j) % 2], end='')

    print()