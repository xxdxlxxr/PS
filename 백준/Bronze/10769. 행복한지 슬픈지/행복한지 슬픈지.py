string, cnt = input(), [0, 0]

for i in range(len(string) - 2):
    if string[i:i + 3] == ':-)':
        cnt[0] += 1
    elif string[i:i + 3] == ':-(':
        cnt[1] += 1

print('none' if sum(cnt) == 0 else 'unsure' if cnt[0] == cnt[1] else 'happy' if cnt[0] > cnt[1] else 'sad')