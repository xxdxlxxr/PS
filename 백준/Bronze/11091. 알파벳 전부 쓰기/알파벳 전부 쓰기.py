for _ in range(int(input())):
    cnt = 26 * [0]

    for char in input():
        if char.isalpha():
            cnt[ord(char.lower()) - ord('a')] += 1

    if cnt.count(0):
        print('missing', end=' ')

        for i in range(26):
            if not cnt[i]:
                print(chr(i + ord('a')), end='')

        print()
    else:
        print('pangram')