while 1:
    submission, answer = input().split(), []

    if submission[0] == '0':
        break

    submission = submission[1:]

    for unit in submission:
        if len(answer) == 0:
            answer.append(unit)
        elif unit != answer[-1]:
            answer.append(unit)

    answer.append('$')

    print(*answer)