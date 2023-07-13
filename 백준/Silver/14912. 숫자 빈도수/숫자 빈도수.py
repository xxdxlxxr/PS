n, d = map(int, input().split())

print(sum([str(i + 1).count(str(d)) for i in range(n)]))