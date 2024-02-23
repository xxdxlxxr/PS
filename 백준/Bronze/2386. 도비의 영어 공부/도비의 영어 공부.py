while 1:
    str = input()

    if str == '#':
        break

    print(str[0], str[1:].lower().count(str[0]))