N = int(input())

for i in range(5):
    for _ in range(N):
        print(N * (1 + 4 * (i % 2 == 0)) * '@')