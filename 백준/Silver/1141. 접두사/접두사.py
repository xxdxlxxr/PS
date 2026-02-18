N = int(input())
words, answer = sorted((input() for _ in range(N)), key=len), 0

for i in range(N):
    check = False

    for j in range(i + 1, N):
        if words[i] == words[j][0:len(words[i])]:
            check = True
            break

    if not check:
        answer += 1

print(answer)