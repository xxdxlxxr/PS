for _ in range(int(input())):
    d, answer = int(input()), 0

    while d >= answer * (answer + 1):
        answer += 1

    print(answer - 1)