N, C = map(int, input().split())
firework = (C + 1) * [0]

for _ in range(N):
    time = int(input())

    if time == 1:
        print(C)
        exit()
    else:
        for i in range(time, C + 1, time):
            firework[i] = 1

print(sum(firework))