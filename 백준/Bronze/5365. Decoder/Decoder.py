n, words = int(input()), input().split()
print(words[0][0], end='')

for i in range(n - 1):
    if len(words[i]) > len(words[i + 1]):
        print(' ', end='')
    else:
        print(words[i + 1][len(words[i]) - 1], end='')