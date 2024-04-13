cnt = 1

while 1:
    o, w = map(int, input().split())
    state = 1

    if not o:
        break

    while 1:
        EF, n = input().split()

        if EF == '#':
            break

        if state:
            w += 2 * (ord(EF) - ord('E') - .5) * int(n)

            if w < 1:
                state = 0

    print(cnt, 'RIP' if not state else ':-)' if o / 2 < w < 2 * o else ':-(')
    cnt += 1