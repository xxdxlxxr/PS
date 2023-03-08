def function():
    N = int(input())
    words = []

    for i in range(N):
        word = input()
        words.append(word)
        cnt = 0

        while cnt < i:
            if word[cnt] != words[cnt][i]:
                return 'NO'

            cnt += 1

    return 'YES'

print(function())