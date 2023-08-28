N, M = input().split()

print(''.join(N[i % len(N)] for i in range(min(int(N) * len(N), int(M)))))