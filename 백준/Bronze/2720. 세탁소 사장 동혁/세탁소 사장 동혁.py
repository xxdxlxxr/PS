for _ in range(int(input())):
    C = int(input())

    for coin in [25, 10, 5, 1]:
        print(C // coin, end=' ')
        C %= coin

    print()