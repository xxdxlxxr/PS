N, arr = int(input()), []

for _ in range(N):
    cards = list(map(int, input().split()))
    tmp = 0

    for i in range(3):
        for j in range(i + 1, 4):
            for k in range(j + 1, 5):
                tmp = max(sum([cards[i], cards[j], cards[k]]) % 10, tmp)

    arr.append(tmp)

print(N - list(reversed(arr)).index(max(arr)))