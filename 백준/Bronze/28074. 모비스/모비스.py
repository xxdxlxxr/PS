str, answer = input(), 1

for char in 'MOBIS':
    if char not in str:
        answer = 0
        break

print('YES' if answer else 'NO')