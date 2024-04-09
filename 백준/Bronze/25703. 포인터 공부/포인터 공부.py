print('int a;')
print('int *ptr = &a;')

for i in range(2, int(input()) + 1):
    print('int {}ptr{} = &ptr'.format(i * '*', i), end='')
    print('' if i == 2 else i - 1, end=';\n')