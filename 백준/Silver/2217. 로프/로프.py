N, answer = int(input()), []

for w in sorted(int(input()) for _ in range(N)):
    answer.append(N * w)
    N -= 1

print(max(answer))