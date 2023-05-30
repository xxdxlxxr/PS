pi, answer = 3.14159, 0

for _ in range(int(input())):
    vol = input().split()

    if vol[0] == 'C':
        tmp = pi * float(vol[1]) ** 2 * float(vol[2]) / 3
    elif vol[0] == 'L':
        tmp = pi * float(vol[1]) ** 2 * float(vol[2])
    else:
        tmp = 4 * pi * float(vol[1]) ** 3 / 3

    answer = max(answer, tmp)

print(f'{answer:.3f}')