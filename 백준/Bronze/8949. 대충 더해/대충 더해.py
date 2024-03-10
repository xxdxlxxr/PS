A, B = input().split()

if len(A) > len(B):
    B = (len(A) - len(B)) * '0' + B
else:
    A = (len(B) - len(A)) * '0' + A

for i in range(len(A)):
    print(int(A[i]) + int(B[i]), end='')