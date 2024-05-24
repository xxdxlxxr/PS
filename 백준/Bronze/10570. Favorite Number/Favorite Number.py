for _ in range(int(input())):
    cnt = {}

    for _ in range(int(input())):
        S = int(input())

        if S not in cnt:
            cnt[S] = 0

        cnt[S] += 1

    print(sorted(cnt.items(), key=lambda x: (-x[1], x[0]))[0][0])