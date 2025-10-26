N, tmp, total = int(input()), [1, 1], 0

for i in range(2, 21):
    tmp.append(i * tmp[i - 1])

for i in range(20, -1, -1):
    if total + tmp[i] < N:
        total += tmp[i]
    elif total + tmp[i] == N:
        print('YES')
        break
else:
    print('NO')