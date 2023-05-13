X, i, sum = int(input()), 1, 0

while X > sum:
    sum += i
    i += 1

if i % 2:
    print(f'{X - sum + i - 1}/{sum - X + 1}')
else:
    print(f'{sum - X + 1}/{X - sum + i - 1}')