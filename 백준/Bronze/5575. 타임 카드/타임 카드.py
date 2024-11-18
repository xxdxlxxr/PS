for _ in range(3):
    time = list(map(int, input().split()))
    answer = [time[3] - time[0], time[4] - time[1], time[5] - time[2]]

    for i in range(2):
        if answer[2 - i] < 0:
            answer[1 - i] -= 1
            answer[2 - i] += 60

    print(*answer)