N, M = map(int, input().split())

for _ in range(N):
    painting = list(input())

    for i in range(M):
        if painting[i].isalpha():
            painting[-(i + 1)] = painting[i]

    print(''.join(painting))