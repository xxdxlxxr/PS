input()
S, answer = input(), 1

for char in 'IOI':
    index = S.find(char)

    if index > -1:
        S = S[index + 1:]
    else:
        answer = 0
        break

print('Yes' if answer else 'No')