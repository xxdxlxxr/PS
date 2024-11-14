N, M = map(int, input().split())
AB = []

for i in range(N):
    row = input().split()

    for j in range(M):
        if row[j] == '1':
            AB.append([i, j])

    if len(AB) == 2:
        break

print(abs(AB[0][0] - AB[1][0]) + abs(AB[0][1] - AB[1][1]))