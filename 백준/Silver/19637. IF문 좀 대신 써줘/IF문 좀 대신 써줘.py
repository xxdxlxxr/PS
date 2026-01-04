import sys

N, M = map(int, sys.stdin.readline().split())
tmp = []

for i in range(N):
    a, b = sys.stdin.readline().split()
    tmp.append([a, int(b)])

tmp.sort(key=lambda x : x[1])

for j in range(M):
    power, start, end = int(sys.stdin.readline()), 0, len(tmp) - 1

    while start <=  end:
        mid = (start + end) // 2

        if power > tmp[mid][1]:
            start = mid + 1
        else:
            end = mid - 1

    print(tmp[start][0])