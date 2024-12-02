n, a, x = int(input()), sorted(list(map(int, input().split()))), int(input())
l, r, cnt = 0, n - 1, 0

while l < r:
    tmp = a[l] + a[r]

    if tmp == x:
        l += 1
        r -= 1
        cnt += 1
    else:
        if tmp < x:
            l += 1
        else:
            r -= 1

print(cnt)