A, B = map(int, input().split())
C, D = map(int, input().split())
print('Either' if A + C == B + D else 'Hanyang Univ.' if A + C < B + D else 'Yongdap')