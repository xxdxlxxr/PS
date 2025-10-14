n, string = int(input()), input()
print(sum(not string[i:i + n // 10].count('N') for i in range(0, n, n // 10)))