answer = 0

for _ in range(int(input())):
    word, cnt = input(), 0

    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            check = word[i + 1:]

            if check.count(word[i]):
                cnt += 1

    if not cnt:
        answer += 1

print(answer)