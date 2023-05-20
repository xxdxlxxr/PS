def solution(a, b, c):
    A = a + b + c
    B = A * (a ** 2 + b ** 2 + c ** 2)
    C = B * (a ** 3 + b ** 3 + c ** 3)
    
    if a == b == c:
        return C
    elif a == b and b != c or a == c and a != b or b == c and a != b:
        return B
    else:
        return A