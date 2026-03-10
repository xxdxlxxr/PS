t, x, m = map(int, input().split())
min_n = 1e9

for i in range(m):
    d, s = map(int, input().split())
    min_n = min(min_n, (d - 1) // s)

print(min_n * x if min_n == 0 else (min_n + (t - min_n)//2) * x if t > min_n else t * x)