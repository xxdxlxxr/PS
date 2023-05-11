A, B, cnt = list(map(int, input().split())), list(map(int, input().split())), 0

for i in range(10):
    if A[i] != B[i]:
        cnt += (A[i] - B[i]) // abs(A[i] - B[i])

print('A' if cnt > 0 else 'B' if cnt < 0 else 'D')