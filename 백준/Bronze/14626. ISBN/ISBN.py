number = input()
sum = sum((2 * (i % 2) + 1) * int(number[i]) if number[i].isnumeric() else 0 for i in range(13))

print(0 if sum % 10 == 0 else [0, 3, 6, 9, 2, 5, 8, 1, 4, 7].index(10 - sum % 10) if number.index('*') % 2 else 10 - sum % 10)