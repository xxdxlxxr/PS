A, B = map(int, input().split())
B += int(input())

if B >= 60:
    temp = B // 60
    A += temp
    B %= 60

    if A >= 24:
        A %= 24

print(A, B)