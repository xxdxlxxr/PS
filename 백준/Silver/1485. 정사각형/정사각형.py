T = int(input())

for i in [[list(map(int, input().split())) for j in range(4)] for i in range(T)]:
    dist = sorted(((v[0] - j[0]) ** 2) + ((v[1] - j[1]) ** 2) for k, v in enumerate(i) for j in i[k + 1:])

    print(int(dist[0] == dist[1] and dist[1] == dist[2] and dist[2] == dist[3] and dist[4] == dist[5]))