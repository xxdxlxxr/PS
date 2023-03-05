N = int(input())
str = list(input())

for i in range(N):
    if str[i].isalpha():
        str[-1 - i] = str[i]

for i in range(N):
    if str[i] == '?':
        str[i] = 'a'

print(''.join(str))