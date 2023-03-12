SY, SM, SD = map(int, input().split())
EY, EM, ED = map(int, input().split())
distance = 30 * (12 * (EY - SY) + EM - SM) + ED - SD
a = 0

for i in range(distance // 360):
    a += 15 + i // 2

print(a, min(distance // 30, 36))
print('{}days'.format(distance))