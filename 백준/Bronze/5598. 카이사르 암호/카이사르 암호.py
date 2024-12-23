for char in input():
    print(chr(ord(char) - 3 + 26 * (char < 'D')), end='')