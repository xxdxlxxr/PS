n, before, after = int(input()), list(input()), list(input())

if n % 2:
    for i in range(len(before)):
        if before[i] == '1':
            before[i] = '0'
        else:
            before[i] = '1'

print('Deletion succeeded' if before == after else 'Deletion failed')