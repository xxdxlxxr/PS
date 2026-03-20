N = int(input())
tips, answer = sorted((int(input()) for _ in range(N)), reverse=True), 0

for i in range(N):
    tmp = tips[i] - i

    if tmp < 0:
        continue

    answer += tmp

print(answer)