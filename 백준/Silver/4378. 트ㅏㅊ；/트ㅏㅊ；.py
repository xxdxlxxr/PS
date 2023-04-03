from sys import stdin

keyboard = '`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./'

while 1:
    sentence = stdin.readline().rstrip()
    answer = ''

    if sentence == '':
        break

    for alphabet in sentence:
        if alphabet == ' ':
            answer += ' '
        else:
            answer += keyboard[keyboard.index(alphabet) - 1]

    print(answer)