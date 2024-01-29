for _ in range(int(input())):
    N, M = map(int, input().split())
    answer = 0

    for i in range(N, M + 1):
        answer += str(i).count('0')

    print(answer)