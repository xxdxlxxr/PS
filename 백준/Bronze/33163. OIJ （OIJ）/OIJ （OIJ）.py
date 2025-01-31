N, S = int(input()), input()

for i in range(N):
    if S[i] == 'J':
        print('O', end='')
    elif S[i] == 'O':
        print('I', end='')
    else:
        print('J', end='')