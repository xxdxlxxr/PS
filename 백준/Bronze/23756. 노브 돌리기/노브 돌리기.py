N, A, answer = int(input()), int(input()), 0

for _ in range(N):
    tmp = int(input())
    answer += min(abs(tmp - A), tmp - A + 360, A - tmp + 360)
    A = tmp

print(answer)