while 1:
    string = input()

    if string == '#':
        break

    print(sum((i + 1) * (ord(char) - ord('A') + 1) for i, char in enumerate(string) if char.isalpha()))