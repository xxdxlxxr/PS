A, B = int(input()), int(input())

if A == B:
    print(0)
else:
    print(int((A - B) / abs(A - B)))