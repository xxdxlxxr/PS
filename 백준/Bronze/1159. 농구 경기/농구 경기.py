cnt, answer = dict(), ''

for _ in range(int(input())):
    first = input()[0]

    if first not in cnt:
        cnt[first] = 0

    cnt[first] += 1

for char in cnt:
    if cnt[char] > 4:
        answer += char

print(''.join(sorted(answer)) if answer else 'PREDAJA')