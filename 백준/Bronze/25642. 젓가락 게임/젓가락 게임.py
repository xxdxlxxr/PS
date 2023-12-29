A, B = map(int, input().split())
order = 1

while max(A, B) < 5:
    if order % 2:
        B += A
    else:
        A += B

    order += 1

print('yj' if A > 4 else 'yt')