N, T = map(int, input().split())
result = []

for _ in range(N):
    S, I, C = map(int, input().split())
    tmp = [S + (I * c) for c in range(C)]

    if tmp[-1] < T:
        continue

    start, end, answer = 0, C - 1, 0

    while start <= end:
        mid = (start + end) // 2

        if tmp[mid] >= T:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    result.append(tmp[answer] - T)

print(min(result) if result else -1)