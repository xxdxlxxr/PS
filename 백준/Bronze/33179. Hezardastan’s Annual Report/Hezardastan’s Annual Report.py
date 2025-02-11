n = int(input())
print(sum(p // 2 + p % 2 for p in map(int, input().split())))