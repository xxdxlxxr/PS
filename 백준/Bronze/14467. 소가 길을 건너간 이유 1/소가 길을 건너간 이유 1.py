record, cnt = {}, 0

for _ in range(int(input())):
    num, loc = map(int, input().split())

    if num in record:
        cnt += record[num] != loc

    record[num] = loc

print(cnt)