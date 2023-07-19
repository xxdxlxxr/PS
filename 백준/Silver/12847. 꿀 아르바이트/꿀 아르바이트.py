n, m = map(int, input().split())
pay = list(map(int, input().split()))
tmp = answer = sum(pay[:m])

for i in range(n - m):
    tmp += pay[i + m] - pay[i]
    answer = max(tmp, answer)

print(answer)