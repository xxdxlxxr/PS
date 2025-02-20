s = input()

for i in range(26):
    for char in s:
        print(chr(ord(char) - i + 26 * (i + ord('A') > ord(char))), end='')

    print()