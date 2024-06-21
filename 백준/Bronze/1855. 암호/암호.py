K, string = int(input()), input()
table = [string[K * i:K * i + K] for i in range(len(string) // K)]
rows = len(table)

for i in range(rows):
    table[i] = table[i][::-2 * (i % 2) + 1]

print(''.join(table[i % rows][i // rows] for i in range(len(string))))