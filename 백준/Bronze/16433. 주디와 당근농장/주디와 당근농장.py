N, R, C = map(int, input().split())

if (R + C) % 2:
    for i in range(N):
        for j in range(N):
            if (i + j) % 2:
                print('v', end = '')
            else:
                print('.', end = '')

        print()
else:
    for i in range(N):
        for j in range(N):
            if (i + j) % 2:
                print('.', end='')
            else:
                print('v', end='')

        print()