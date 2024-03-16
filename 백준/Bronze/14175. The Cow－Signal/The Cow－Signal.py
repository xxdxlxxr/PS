N, M, K = map(int, input().split())

for _ in range(N):
    string = input()

    for _ in range(K):
        print(''.join(K * char for char in string))