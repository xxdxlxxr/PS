n, d = map(int, input().split())
problems = [int(input()) for _ in range(n)]
total = sum(problems)

for unit in problems:
    print(d * unit // total)