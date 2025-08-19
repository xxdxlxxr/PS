N, answer = int(input()), 0

for i in range(2, N - 1, 2):
    answer += (N - i - 2) // 2

print(answer)