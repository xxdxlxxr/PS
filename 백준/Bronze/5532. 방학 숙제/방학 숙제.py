L, A, B, C, D = int(input()), int(input()), int(input()), int(input()), int(input())

print(L - max(A // C + (A % C != 0), B // D + (B % D != 0)))