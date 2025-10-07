total = 0

for _ in range(8):
    for char in input():
        tmp = 1 if char in 'Pp' else 3 if char in 'NnBb' else 5 if char in 'Rr' else 9 if char in 'Qq' else 0
        total += (2 * char.isupper() - 1) * tmp

print(total)