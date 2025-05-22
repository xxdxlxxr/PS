K, N = map(int, input().split())
length = [int(input()) for _ in range(K)]
start, end = 1, max(length)

while start <= end:
    mid, lines = (start + end) // 2, 0

    for i in length:
        lines += i // mid

    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)