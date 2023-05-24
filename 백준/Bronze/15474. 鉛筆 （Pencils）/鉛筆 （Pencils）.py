N, A, B, C, D = map(int, input().split())

print(min((N // A + (N % A != 0)) * B, (N // C + (N % C != 0)) * D))