for _ in range(int(input())):
    rank = sorted(list(map(int, input().split())) for _ in range(int(input())))
    tmp = 0
    answer = 1

    for i in range(1, len(rank)):
        if rank[i][1] < rank[tmp][1]:
            tmp = i
            answer += 1

    print(answer)