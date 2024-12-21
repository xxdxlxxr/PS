while 1:
    scores = input()

    if scores == '#':
        break

    cnt, tmp = 2 * [0], 2 * [0]

    for win in scores:
        tmp[win == 'B'] += 1

        if max(tmp) > 3 and abs(tmp[0] - tmp[1]) > 1:
            if tmp[0] > tmp[1]:
                cnt[0] += 1
            else:
                cnt[1] += 1

            tmp = 2 * [0]

    print('A', cnt[0], 'B', cnt[1])