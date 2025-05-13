record, cnt = set(), 0

for _ in range(int(input())):
    word = input()

    if word != 'ENTER':
        if word not in record:
            cnt += 1
            record.add(word)
    elif word == 'ENTER':
        record.clear()

print(cnt)