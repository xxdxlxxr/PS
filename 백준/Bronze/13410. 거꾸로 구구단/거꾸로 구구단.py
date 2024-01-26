N, K = map(int, input().split())

print(max(int(''.join(reversed(str((i + 1) * N)))) for i in range(K)))