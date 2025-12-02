N, M = map(int,input().split())

if N == 0:
    print(0)
else:
    weight, cnt = 0, 1

    for box in map(int,input().split()):
        if box + weight <= M:
            weight += box
        else :
            weight = box
            cnt += 1

    print(cnt)