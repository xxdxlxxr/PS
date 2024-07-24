H, W = map(int, input().split())

for _ in range(H):
    clouds, tmp, pred = input(), -1, []

    for cloud in clouds:
        if cloud == 'c':
            tmp = 0
        elif tmp + 1:
            tmp += 1

        pred.append(tmp)

    print(*pred)