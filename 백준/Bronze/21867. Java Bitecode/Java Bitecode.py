N, S = int(input()), input()

for char in 'JAV':
    S = S.replace(char, '')

print(S if S else 'nojava')