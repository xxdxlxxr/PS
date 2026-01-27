for _ in range(int(input())):
    input()
    A, B, C, D = map(int, input().split())
    A, B, C = sorted((A, B, C))
    s = A + B + C - D
    tmp = min(s // 3, A)
    a1 = tmp
    s -= tmp
    tmp = min(s // 2, B)
    print(a1 * tmp * (s - tmp))