while 1:
    string = input()

    if string == '#':
        break

    print(sum(-1 * 8 ** i if string[-(i + 1)] == '/' else ['-', '\\', '(', '@', '?', '>', '&', '%'].index(string[-(i + 1)]) * 8 ** i for i in range(len(string))))