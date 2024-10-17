A, B = sorted(map(int, input().split()))
print(max(B - A - 1, 0))
print(*(i for i in range(A + 1, B)))