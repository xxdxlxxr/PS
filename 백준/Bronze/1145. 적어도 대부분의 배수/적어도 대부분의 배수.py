nums = list(map(int, input().split()))
m = min(nums)

while 1:
    cnt = 0

    for i in nums:
        if m % i == 0:
            cnt += 1

    if cnt > 2:
        break

    m += 1

print(m)