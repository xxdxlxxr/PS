A, B = list(map(int, input().split())), list(map(int, input().split()))

while A[1] * B[1] != 0:
    A[1] = max(A[1] - B[0], 0)
    B[1] = max(B[1] - A[0], 0)

print('DRAW' if A[1] + B[1] == 0 else 'PLAYER A' if A[1] else 'PLAYER B')