for _ in range(int(input())):
    N, food, answer = int(input()), sum(list(map(int, input().split()))), 1

    while N >= food:
        answer += 1
        food *= 4

    print(answer)