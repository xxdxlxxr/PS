for _ in range(int(input())):
    P, M = map(int, input().split())
    seats, answer = M * [0], 0

    for i in range(P):
        wish = int(input())

        if not seats[wish - 1]:
            seats[wish - 1] = 1
        else:
            answer += 1

    print(answer)