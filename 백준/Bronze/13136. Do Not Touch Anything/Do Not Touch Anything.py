R, C, N = map(int, input().split())
print((R // N + (R % N != 0)) * (C // N + (C % N != 0)))