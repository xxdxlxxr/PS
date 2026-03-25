for _ in range(int(input())):
    W, N = map(int, input().split())
    tmp = [list(map(int, input().split())) for _ in range(N)]
    capacity, previous_value, answer = 0, 0, 0
    
    for i in tmp:
        if capacity + i[1] < W:
            answer += i[0] - previous_value
            capacity += i[1]
        elif capacity + i[1] == W:
            answer += i[0] - previous_value + 2 * i[0]
            capacity = 0
            if tmp.index(i) == N - 1:
                answer -= 2 * i[0]
        elif capacity + i[1] > W:
            capacity = i[1]
            answer += i[0] - previous_value + 2 * i[0]

        previous_value = i[0]

    if tmp.index(i) == N - 1:
        answer += i[0]

    print(answer)