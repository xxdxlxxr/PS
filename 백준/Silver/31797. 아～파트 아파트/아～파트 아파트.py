N, M = map(int, input().split())
tmp = []

for i in range(M):
    l, r = map(int, input().split())
    tmp.append([l, i + 1])
    tmp.append([r, i + 1])

tmp.sort(key= lambda x: x[0])
print(tmp[N % (2 * M) - 1][1])