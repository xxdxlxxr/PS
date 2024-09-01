A, B = map(int, input().split())
R = B - A + 1

if A % 2 == 0:
    R -= 1

if B % 2:
    R -= 1

print(R // 2 + (A % 2 == 0) + (B % 2))