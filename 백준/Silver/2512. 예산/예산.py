N, cities, budgets = int(input()), list(map(int, input().split())), int(input())
start, end = 0, max(cities)

while start <= end:
    mid, total = (start + end) // 2, 0

    for i in cities:
        if i > mid:
            total += mid
        else:
            total += i

    if total <= budgets:
        start = mid + 1
    else:
        end = mid - 1

print(end)