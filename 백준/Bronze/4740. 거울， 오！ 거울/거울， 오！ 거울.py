while 1:
    string = input()

    if string == '***':
        break

    print(''.join(reversed(string)))