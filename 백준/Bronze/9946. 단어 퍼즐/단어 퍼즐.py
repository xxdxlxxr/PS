cnt = 1

while 1:
    word1, word2 = input(), input()

    if word1 == 'END' and word2 == 'END':
        break

    print(f'Case {cnt}:', 'same' if sorted(word1) == sorted(word2) else 'different')
    cnt += 1