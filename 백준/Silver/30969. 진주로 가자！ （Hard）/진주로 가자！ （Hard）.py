costs, cnt = 1001 * [0], 0

for _ in range(int(input())):
    city, cost = input().split()
    cost = int(cost)

    if city == 'jinju':
        target = cost
    elif cost > 1000:
        cnt += 1
    else:
        costs[cost] += 1

cnt += sum(costs[i] for i in range(target + 1, 1001))
print(target)
print(cnt)