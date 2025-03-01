N, M = map(int, input().split())
tmp = int(24 * 60 * M / N)
print(f'{tmp // 60:02d}:{tmp % 60:02d}')