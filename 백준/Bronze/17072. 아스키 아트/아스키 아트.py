N, M = map(int, input().split())

for _ in range(N):
    pixel = list(map(int, input().split()))
    answer = ''

    for i in range(M):
        tmp = 2126 * pixel[3 * i] + 7152 * pixel[3 * i + 1] + 722 * pixel[3 * i + 2]
        answer += chr(35 if tmp < 510000 else 111 if tmp < 1020000 else 43 if tmp < 1530000 else 45 if tmp < 2040000 else 46)

    print(answer)