results = []

for i in range(int(input())):
    N, A, D = map(int, input().split())
    results.append(N * A + D * (N * (N - 1)) // 2)

for result in results:
    print(result)