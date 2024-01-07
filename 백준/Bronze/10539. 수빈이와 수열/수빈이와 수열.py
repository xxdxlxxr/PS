N, B = int(input()), list(map(int, input().split()))
answer = [B[0]]

for i in range(N - 1):
    answer.append((i + 2) * B[i + 1] - (i + 1) * B[i])

print(*answer)