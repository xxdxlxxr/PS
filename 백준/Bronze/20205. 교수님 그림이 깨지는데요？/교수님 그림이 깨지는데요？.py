N, K = map(int, input().split())

for _ in range(N):
    numbers = map(int, input().split())
    arr = []

    for number in numbers:
        arr += K * [number]

    for _ in range(K):
        print(*arr)