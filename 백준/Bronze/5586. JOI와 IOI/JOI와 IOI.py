s, cnt = input(), [0, 0]

for i in range(len(s) - 2):
    if s[i:i + 3] == 'JOI':
        cnt[0] += 1
    elif s[i:i + 3] == 'IOI':
        cnt[1] += 1

print(cnt[0])
print(cnt[1])