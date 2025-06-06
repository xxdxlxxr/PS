while 1:
    NP = list(map(int, input().split()))

    if NP == [0]:
        break

    for i in range(NP[0] // 4):
        tmp = [2 * i + 1, 2 * i + 2, NP[0] - 2 * i - 1, NP[0] - 2 * i]

        if NP[1] in tmp:
            tmp.remove(NP[1])
            print(*tmp)