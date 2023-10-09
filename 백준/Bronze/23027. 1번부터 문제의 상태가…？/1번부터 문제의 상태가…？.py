S = input()

if 'A' in S:
    for char in 'BCDF':
        S = S.replace(char, 'A')
elif 'B' in S:
    for char in 'CDF':
        S = S.replace(char, 'B')
elif 'C' in S:
    for char in 'DF':
        S = S.replace(char, 'C')
else:
    S = len(S) * 'A'

print(S)