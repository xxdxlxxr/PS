for i in range(1, int(input()) + 1):
    print(f'String #{i}')

    for char in input():
        print(chr((ord(char) - ord('A') + 1) % 26 + ord('A')), end='')

    print()
    print()