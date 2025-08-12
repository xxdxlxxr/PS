while 1:
    M, A, B = map(int, input().split())

    if M == A == B == 0:
        break

    tmp = round((M / A - M / B) * 3600)
    print("%d:%02d:%02d" % (tmp // 3600, tmp % 3600 // 60, tmp % 60))