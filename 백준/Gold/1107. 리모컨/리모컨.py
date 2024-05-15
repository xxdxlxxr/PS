N, M = int(input()), int(input())
broken, answer = list(map(int, input().split())) if M else [], abs(N - 100)

for i in range(10 ** 6):
    for j in str(i):
        if int(j) in broken:
            break
    else:
        answer = min(abs(N - i) + len(str(i)), answer)

print(answer)