while 1:
    a1, a2, a3 = map(int, input().split())

    if (a1, a2, a3) == (0, 0, 0):
        break

    if a1 + a3 == 2 * a2:
        print('AP', 2 * a3 - a2)
    else:
        print('GP', a3 ** 2 // a2)