while 1:
    string = input()

    if string == 'END':
        break

    print(''.join(reversed(string)))