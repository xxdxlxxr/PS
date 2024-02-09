while 1:
    a, b, c, d = map(int, input().split())

    if [a, b, c, d] == 4 * [0]:
        break

    print(c - b, d - a)