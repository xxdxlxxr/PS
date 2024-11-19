a, b, c = map(int, input().split())
print(sum([a, b, c]) - max(a, b, c) + min(sum([a, b, c]) - max(a, b, c) - 1, max(a, b, c)))