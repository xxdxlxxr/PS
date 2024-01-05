N, M = map(int, input().split())
K = list(map(int, input().split()))
answer = 0

for num in range(1, N + 1):
    check = 0

    for k in K:
        if num % k == 0:
            check = 1
            break

    answer += check * num

print(answer)