for _ in range(int(input())):
    N, tmp = int(input()), 0

    for _ in range(N):
        univ, consumption = input().split()

        if int(consumption) > tmp:
            tmp = int(consumption)
            answer = univ

    print(answer)