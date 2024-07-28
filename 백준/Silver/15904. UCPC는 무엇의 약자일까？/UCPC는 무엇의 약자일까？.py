s, tmp = input().replace(' ', ''), 0

for char in s:
    if char == 'UCPC'[tmp]:
        tmp += 1

    if tmp == 4:
        print('I love UCPC')
        break
else:
    print('I hate UCPC')