N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:
    mid, tmp = (start + end) // 2, 0

    for i in tree:
        if i >= mid:
            tmp += i - mid

    if tmp >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)