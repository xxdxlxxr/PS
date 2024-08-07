cnt = 1

while 1:
    n = int(input())

    if not n:
        break

    print(cnt)

    for track in sorted(input() for _ in range(n)):
        print(track)

    cnt += 1