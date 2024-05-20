X, L, R = map(int, input().split())

print(L if X < L else X if X < R else R)