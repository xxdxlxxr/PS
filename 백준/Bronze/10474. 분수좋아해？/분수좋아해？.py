while 1:
    nu, de = map(int, input().split())

    if nu * de == 0:
        break

    print(f'{nu // de} {nu % de} / {de}')