while 1:
    string = input()

    if string == '#':
        break

    print(string[:-1], end='')
    print(int(sum(map(int, string[:-1])) % 2 == (string[-1] == 'e')))