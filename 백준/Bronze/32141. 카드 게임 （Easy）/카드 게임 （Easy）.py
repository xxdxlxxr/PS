N, H = map(int, input().split())
d = list(map(int, input().split()))

for i in range(N):
    H -= d[i]

    if H <= 0:
        print(i + 1)
        break
else:
    print(-1)