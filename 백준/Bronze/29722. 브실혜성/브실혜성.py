y, m, d = map(int, input().split('-'))
d += int(input())
m += (d - 1) // 30
d = (d - 1) % 30 + 1
y += (m - 1) // 12
m = (m - 1) % 12 + 1
print(f'{y}-{m:02d}-{d:02d}')