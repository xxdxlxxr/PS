cnt = 0

for _ in range(6):
    if input() == 'W':
        cnt += 1

print((6 - cnt) // 2 + 1 if cnt else -1)