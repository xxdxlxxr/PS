N, M = map(int, input().split())
A = list(map(int, input().split()))
l, r, cnt = 0, 1, 0

while r <= N and l <= r:
    tmp = sum(A[l:r])

    if tmp == M:
        cnt += 1
        r += 1
    elif tmp < M:
        r += 1
    else:
        l += 1

print(cnt)