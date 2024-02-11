while 1:
    N = input()

    if int(N):
        print(4 * len(N) + N.count('0') - N.count('1') + 1)
    else:
        break