N, M = map(int, input().split())
expense = list(int(input()) for _ in range(N))
l, r = min(expense), sum(expense)

while l <= r:
    mid = (l + r) // 2
    charge, tmp = mid, 1

    for i in range(N):
        if charge < expense[i]:
            charge = mid
            tmp += 1

        charge -= expense[i]

    if tmp > M or mid < max(expense):
        l = mid + 1
    else:
        r = mid - 1
        answer = mid

print(answer)