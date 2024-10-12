tmp, cnt = 1000 - int(input()), 0

for change in [500, 100, 50, 10, 5, 1]:
    cnt += tmp // change
    tmp %= change

print(cnt)