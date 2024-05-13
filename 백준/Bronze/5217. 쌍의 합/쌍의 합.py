for _ in range(int(input())):
    n = int(input())
    pairs = [[i, n - i] for i in range(1, n // 2 + (n % 2 != 0))]

    print(f'Pairs for {n}: ', end='')

    for i in range(len(pairs)):
        print(pairs[i][0], pairs[i][1], end='')

        if i + 1 != len(pairs):
            print(', ', end='')

    print()