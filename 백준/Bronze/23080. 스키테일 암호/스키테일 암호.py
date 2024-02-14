K = int(input())
print(''.join(char if i % K == 0 else '' for i, char in enumerate(input())))