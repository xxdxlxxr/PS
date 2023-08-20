N = int(input())

for i in range(5):
    for _ in range(N):
        print(N * '@', end='')

        if i in [2, 4]:
            print(3 * N * '@', end='')
        else:
            print(3 * N * ' ', end='')

        print(N * '@')