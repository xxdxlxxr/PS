N, end, total, cnt = int(input()), 0, 0, 0

for i in range(0, N):
    while total < N and end < N:
        total += end + 1
        end += 1

    cnt += total == N
    total -= i + 1

print(cnt)