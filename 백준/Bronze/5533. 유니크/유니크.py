N, numbers = int(input()), [[], [], []]
scores = N * [0]

for _ in range(N):
    number = list(map(int, input().split()))

    for i in range(3):
        numbers[i].append(number[i])

for i in range(3):
    for j in range(N):
        if numbers[i].count(numbers[i][j]) == 1:
            scores[j] += numbers[i][j]

for i in range(N):
    print(scores[i])