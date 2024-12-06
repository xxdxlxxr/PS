cd, cnt = '*' + input(), 1

for i in range(len(cd) - 1):
    cnt *= 16 * (cd[i + 1] == 'c') + 10 - (cd[i] == cd[i + 1])

print(cnt)