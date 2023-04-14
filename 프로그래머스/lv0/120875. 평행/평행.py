def solution(dots):
    A, B, C, D = dots[0], dots[1], dots[2], dots[3]
    
    if (A[0] - B[0]) / (A[1] - B[1]) == (C[0] - D[0]) / (C[1] - D[1]):
        return 1
    elif (A[0] - C[0]) / (A[1] - C[1]) == (B[0] - D[0]) / (B[1] - D[1]):
        return 1
    elif (A[0] - D[0]) / (A[1] - D[1]) == (B[0] - C[0]) / (B[1] - C[1]):
        return 1
    else:
        return 0