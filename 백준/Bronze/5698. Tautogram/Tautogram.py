while 1:
    words, answer = input().split(), 0

    if words == ['*']:
        break

    for i in range(len(words) - 1):
        if words[i][0].lower() != words[i + 1][0].lower():
            answer = 1
            break

    print('YN'[answer])