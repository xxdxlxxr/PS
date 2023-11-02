L, P = map(int, input().split())

print(*(num - L * P for num in list(map(int, input().split()))))