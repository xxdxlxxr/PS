N, P = int(input()), list(map(int, input().split()))
tmp, size = 0, []

for i in range(N - 1):
    if P[i] < P[i + 1]:
        tmp += P[i + 1] - P[i]
    else:
        size.append(tmp)
        tmp = 0

size.append(tmp)
print(max(size))