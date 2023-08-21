N = int(input())

if N % 2:
    print(N * '*')

    for i in range(N // 2 + 1):
        for j in range(N // 2 + i + 1):
            if abs(N // 2 - j) == i:
                print('*', end='')
            else:
                print(' ', end='')

        print()
else:
    print('I LOVE CBNU')