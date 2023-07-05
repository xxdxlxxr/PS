a, b = map(int, input().split())
tmp = 1

for i in range(a, b + 1):
    tmp *= i * (i + 1)

print(tmp // 2 ** (b - a + 1) % 14579)