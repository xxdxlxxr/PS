while 1:
    N, max, answer = int(input()), 0, []

    if not N:
        break

    for _ in range(N):
        name, height = input().split()

        if float(height) > max:
            answer = [name]
            max = float(height)
        elif float(height) == max:
            answer.append(name)

    print(*answer)