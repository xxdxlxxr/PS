h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
t1, t2 = 60 * 60 * h1 + 60 * m1 + s1, 60 * 60 * h2 + 60 * m2 + s2
t = t2 - t1 if t2 > t1 else t2 - t1 + 24 * 60 * 60
print(f'{t // 60 // 60:02d}:{t // 60 % 60:02d}:{t % 60:02d}')