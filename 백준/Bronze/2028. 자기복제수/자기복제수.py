for _ in range(int(input())):
    N = input()

    print('YES' if str(int(N) ** 2)[-len(N):] == N else 'NO')