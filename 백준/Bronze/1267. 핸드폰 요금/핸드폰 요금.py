N, Y, M = int(input()), 0, 0

for t in map(int, input().split()):
    Y += (t // 30 + 1) * 10
    M += (t // 60 + 1) * 15

if Y == M:
    print('Y M', Y)
elif Y < M:
    print('Y', Y)
else:
    print('M', M)