N, numbers, answer = int(input()), list(map(int, input().split())), []

for i in range(N):
    answer.insert(i - numbers[i], i + 1)

print(*answer)