for _ in range(int(input())):
    n = int(input())
    loc = sorted(list(map(int, input().split())))

    print(2 * (loc[-1] - loc[0]))