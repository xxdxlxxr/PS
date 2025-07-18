N, M, K = map(int, input().split())
answer = 0

while 1:
    N -= 2
    M -= 1

    if N < 0 or M < 0 or N + M < K:
        break

    answer += 1

print(answer)