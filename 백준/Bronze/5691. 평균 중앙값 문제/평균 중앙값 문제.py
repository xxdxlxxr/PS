while 1:
    A, B = map(int, input().split())

    if not A:
        break

    print(2 * A - B)