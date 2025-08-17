N, i, tmp = int(input()), 1, False

while 1:
    N -= i
    i += 1
    tmp = not tmp

    if N < 0:
        if tmp:
            print(abs(N))
        else:
            print(0)
        break