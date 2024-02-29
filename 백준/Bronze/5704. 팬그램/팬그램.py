while 1:
    str, arr = input(), 26 * [0]

    if str == '*':
        break

    for char in str:
        if char.isalpha():
            arr[ord(char) - ord('a')] = 1

    print('Y' if sum(arr) == 26 else 'N')