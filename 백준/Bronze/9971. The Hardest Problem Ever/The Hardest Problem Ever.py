while 1:
    start = input()

    if start[0] == 'E':
        break

    message = input()

    for alpha in message:
        if alpha.isalpha():
            print(chr(ord(alpha) - 5 + 26 * (ord(alpha) < 70)), end = '')
        else:
            print(alpha, end = '')

    print()

    end = input()