h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
t = 60 * 60 * h2 + 60 * m2 + s2 - (60 * 60 * h1 + 60 * m1 + s1)

if t < 0:
    t += 24 * 60 * 60

h = t // (60 * 60)
m = (t % (60 * 60)) // 60
s = t % 60
print(f'{h:02d}:{m:02d}:{s:02d}')