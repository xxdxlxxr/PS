X, Y = map(int, input().split())
print(abs(X - Y) * '1' + min(X, Y) * '2')