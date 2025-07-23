m, n, cnt = int(input()), int(input()), 0

for i in range(m, n + 1):
    s, number = str(i), ''

    for c in s[::-1]:
        if c in '23457':
            break

        if c in '018':
            number += c
            continue

        if c == '6':
            number += '9'
            continue

        if c == '9':
            number += '6'
            continue

    if number == s:
        cnt += 1

print(cnt)