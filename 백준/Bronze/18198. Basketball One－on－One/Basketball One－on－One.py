record, cnt = input(), [0, 0]

for i in range(len(record) // 2):
    cnt[record[2 * i] == 'B'] += int(record[2 * i + 1])

    if max(cnt) > 10 and abs(cnt[0] - cnt[1]) > 1:
        print('AB'[cnt[0] < cnt[1]])
        break