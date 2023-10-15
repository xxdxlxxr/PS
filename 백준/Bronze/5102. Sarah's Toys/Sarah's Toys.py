while 1:
    owns, left = map(int, input().split())
    answer = [0, 0]

    if owns + left == 0:
        break

    if (owns - left) % 2 == 0:
        answer[0] = (owns - left) // 2
    elif owns - left > 2:
        answer[0] = (owns - left) // 2 - 1
        answer[1] = 1

    print(*answer)