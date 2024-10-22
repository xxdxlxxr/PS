a, b, c = map(int, input().split())
print(c ** 2 - b if a == 0 else c ** 2 - a if b == 0 else int((a + b) ** .5))