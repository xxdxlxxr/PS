while 1:
    abcd = list(map(int, input().split()))
    answer = 0

    if not sum(abcd):
        break

    while len(set(abcd)) != 1:
        abcd += [abcd[0]]
        abcd = [abs(abcd[i] - abcd[i + 1]) for i in range(4)]
        answer += 1

    print(answer)