A, B = input().split()

for i in range(len(A)):
    if B.find(A[i]) > -1:
        col_check = i
        break

row_check = B.index(A[col_check])

for row in range(len(B)):
    print(A if row == row_check else col_check * '.' + B[row] + (len(A) - col_check - 1) * '.')