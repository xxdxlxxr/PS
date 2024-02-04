while 1:
    n = int(input())

    if n:
        print('TENTE NOVAMENTE' if n % 42 else 'PREMIADO')
    else:
        break