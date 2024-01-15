n = input()

if len(n) % 3:
    n = (3 - len(n) % 3) * '0' + n

print(''.join(str(int(n[3 * i:3 * (i + 1)], 2)) for i in range(len(n) // 3)))