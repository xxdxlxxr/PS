N, Q = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0

for _ in range(Q):
    nums = list(map(int, input().split()))

    if nums[0] == 1:
        a[(cnt + nums[1] - 1) % N] += nums[2]
    elif nums[0] == 2:
        cnt -= nums[1]
    else:
        cnt += nums[1]

for i in range(cnt, cnt + N):
    print(a[i % N], end = ' ')